import os
# First install required packages
!apt-get install -y tesseract-ocr
!pip install pytesseract gradio opencv-python-headless pillow numpy

import gradio as gr
from PIL import Image
import numpy as np
import cv2
import os
import pytesseract
import traceback

# Path where your .traineddata files are stored
MODEL_PATH = os.path.dirname(os.path.abspath(__file__))
os.environ["TESSDATA_PREFIX"] = MODEL_PATH

# Check Tesseract
try:
    version = pytesseract.get_tesseract_version()
    print(f"Tesseract version: {version}")
    TESSERACT_LOADED = True
except Exception as e:
    print(f"Tesseract not found: {e}")
    TESSERACT_LOADED = False

# Check available language files
def check_available_languages():
    available = []
    if os.path.exists(MODEL_PATH):
        for f in os.listdir(MODEL_PATH):
            if f.endswith(".traineddata"):
                lang = f.replace(".traineddata", "")
                available.append(lang)
    return available

available_langs = check_available_languages()
print(f"Available languages: {available_langs}")

DEFAULT_LANG = "nawadraat_urdu" if "nawadraat_urdu" in available_langs else "urd"
print(f"Default language: {DEFAULT_LANG}")

import warnings
warnings.filterwarnings("ignore")
# Fixed settings (no UI controls)
PREPROCESS_MODE = "standard"
PSM = "3"

# ── Image Preprocessing ────────────────────────────────────────────────────────
def preprocess_image(image, mode="standard"):
    if image.mode != "RGB":
        image = image.convert("RGB")

    img_array = np.array(image, dtype=np.uint8)

    if mode == "none":
        return Image.fromarray(img_array)

    if mode == "binarize":
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        rgb = cv2.cvtColor(binary, cv2.COLOR_GRAY2RGB)
        return Image.fromarray(rgb)

    if mode == "denoise":
        denoised = cv2.fastNlMeansDenoisingColored(img_array, None, 10, 10, 7, 21)
        gray = cv2.cvtColor(denoised, cv2.COLOR_RGB2GRAY)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        rgb = cv2.cvtColor(binary, cv2.COLOR_GRAY2RGB)
        return Image.fromarray(rgb)

    # Standard mode
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharpened = cv2.filter2D(img_array, -1, kernel)
    sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)

    lab = cv2.cvtColor(sharpened, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l = clahe.apply(l)
    lab = cv2.merge([l, a, b])
    enhanced = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)

    return Image.fromarray(enhanced)

# ── OCR Functions ──────────────────────────────────────────────────────────────
def perform_ocr(image):
    if not TESSERACT_LOADED:
        return "Tesseract not installed. Run: !apt-get install -y tesseract-ocr"

    if image is None:
        return "Please upload an image."

    try:
        processed = preprocess_image(image, mode=PREPROCESS_MODE)
        config = f"--oem 1 --psm {PSM}"
        text = pytesseract.image_to_string(
            processed,
            lang=DEFAULT_LANG,
            config=config
        )
        text = text.strip()
        return text if text else "No text detected. Try different preprocessing or PSM mode."

    except pytesseract.TesseractError as e:
        return f"Tesseract Error: {str(e)}"
    except Exception as e:
        traceback.print_exc()
        return f"Error: {str(e)}"


def perform_ocr_with_confidence(image):
    if not TESSERACT_LOADED:
        return "Tesseract not installed.", "N/A"

    if image is None:
        return "Please upload an image.", "N/A"

    try:
        processed = preprocess_image(image, mode=PREPROCESS_MODE)
        config = f"--oem 1 --psm {PSM}"

        data = pytesseract.image_to_data(
            processed,
            lang=DEFAULT_LANG,
            config=config,
            output_type=pytesseract.Output.DICT
        )

        words = []
        confidences = []
        for i, word in enumerate(data["text"]):
            conf = int(data["conf"][i])
            if conf > 0 and word.strip():
                words.append(word)
                confidences.append(conf)

        text = " ".join(words)
        avg_conf = round(sum(confidences) / len(confidences), 1) if confidences else 0

        result_text = text if text else "No text detected."
        conf_text = f"Confidence: {avg_conf}%  •  {len(words)} words found"

        return result_text, conf_text

    except Exception as e:
        traceback.print_exc()
        return f"Error: {str(e)}", "N/A"

# ── Custom CSS ─────────────────────────────────────────────────────────────────
CSS = """
/* ====== GLOBAL ====== */
.gradio-container {
    max-width: 1100px !important;
    margin: 0 auto !important;
    font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
    background: #020617 !important;
}

/* ====== HEADER ====== */
.main-header {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
    border: 1px solid #312e81;
    border-radius: 20px;
    padding: 28px 24px;
    margin-bottom: 28px;
    text-align: center;
    box-shadow: 0 0 50px -12px rgba(99, 102, 241, 0.3);
    position: relative;
    overflow: hidden;
}

.main-header::before {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at center, rgba(99, 102, 241, 0.1) 0%, transparent 60%);
    pointer-events: none;
}

.main-header h1 {
    font-size: 2.5rem !important;
    font-weight: 800 !important;
    background: linear-gradient(90deg, #67e8f9, #a5b4fc, #c4b5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 0 8px 0 !important;
    letter-spacing: -1px;
    position: relative;
}

.main-header p {
    color: #94a3b8 !important;
    font-size: 1.05rem !important;
    margin: 0 !important;
    position: relative;
}

/* ====== EQUAL HEIGHT BOXES ====== */
.image-box {
    border-radius: 16px !important;
    overflow: hidden !important;
    border: 1px solid #1e293b !important;
    background: #0f172a !important;
}

.urdu-box textarea {
    height: 420px !important;
    min-height: 420px !important;
    max-height: 420px !important;
    direction: rtl !important;
    font-family: 'Noto Nastaliq Urdu', 'Jameel Noori Nastaleeq', 'Noto Naskh Arabic', serif !important;
    font-size: 22px !important;
    line-height: 2.15 !important;
    text-align: right !important;
    background: #0f172a !important;
    border: 1px solid #1e293b !important;
    border-radius: 16px !important;
    padding: 20px 22px !important;
    color: #f1f5f9 !important;
    resize: none !important;
    box-shadow: inset 0 0 0 1px rgba(99, 102, 241, 0.08);
}

/* Confidence */
.confidence-box textarea {
    font-family: 'Inter', monospace !important;
    font-size: 14.5px !important;
    font-weight: 500 !important;
    color: #67e8f9 !important;
    background: #0f172a !important;
    border: 1px solid #164e63 !important;
    border-radius: 12px !important;
    text-align: center !important;
}

/* ====== BUTTONS ====== */
button.primary {
    background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
    border: none !important;
    font-weight: 600 !important;
    letter-spacing: 0.3px;
    border-radius: 12px !important;
    box-shadow: 0 4px 20px rgba(124, 58, 237, 0.35);
    transition: all 0.22s ease !important;
}

button.primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 28px rgba(124, 58, 237, 0.5);
}

button.secondary {
    background: #1e293b !important;
    border: 1px solid #334155 !important;
    color: #e2e8f0 !important;
    border-radius: 12px !important;
}

/* ====== FOOTER ====== */
.footer {
    text-align: center;
    margin-top: 36px;
    padding: 18px;
    color: #64748b;
    font-size: 13px;
    border-top: 1px solid #1e293b;
}
"""

# ── Theme ──────────────────────────────────────────────────────────────────────
theme = gr.themes.Soft(
    primary_hue="violet",
    secondary_hue="slate",
    neutral_hue="slate",
    font=[gr.themes.GoogleFont("Inter"), "ui-sans-serif", "system-ui", "sans-serif"],
).set(
    body_background_fill="#020617",
    body_background_fill_dark="#020617",
    block_background_fill="#0f172a",
    block_background_fill_dark="#0f172a",
    block_border_width="1px",
    block_border_color="#1e293b",
    block_label_text_color="#e2e8f0",
    block_title_text_color="#f8fafc",
    input_background_fill="#0f172a",
    input_border_color="#334155",
    button_primary_background_fill="linear-gradient(135deg, #4f46e5, #7c3aed)",
    button_primary_background_fill_hover="linear-gradient(135deg, #4338ca, #6d28d9)",
)

# ── Gradio UI ──────────────────────────────────────────────────────────────────
with gr.Blocks(title="Urdu OCR", theme=theme, css=CSS) as demo:

    # Header
    gr.HTML("""
        <div class="main-header">
            <h1>Urdu OCR</h1>
            <p>Urdu text extraction from Images</p>
        </div>
    """)

    # Main equal-height area
    with gr.Row(equal_height=True):
        with gr.Column(scale=1, min_width=380):
            single_img = gr.Image(
                type="pil",
                label="Upload Image",
                height=420,
                elem_classes=["image-box"]
            )

        with gr.Column(scale=1, min_width=380):
            single_out = gr.Textbox(
                label="Extracted Urdu Text",
                lines=18,
                rtl=True,
                elem_classes=["urdu-box"],
                placeholder="اردو متن یہاں ظاہر ہوگا..."
            )

    # Buttons
    with gr.Row():
        single_btn = gr.Button(
            "✦ Extract Text",
            variant="primary",
            size="lg",
            scale=2
        )
        single_btn_conf = gr.Button(
            "Extract + Confidence",
            variant="secondary",
            size="lg",
            scale=1
        )

    # Confidence
    confidence_out = gr.Textbox(
        label="Confidence Score",
        lines=1,
        interactive=False,
        elem_classes=["confidence-box"],
        placeholder="Confidence will appear here"
    )

    # Events
    single_btn.click(
        fn=perform_ocr,
        inputs=[single_img],
        outputs=single_out,
    )

    single_btn_conf.click(
        fn=perform_ocr_with_confidence,
        inputs=[single_img],
        outputs=[single_out, confidence_out],
    )

    # Footer
    gr.HTML("""
        <div class="footer">
            Built with Gradio + Tesseract • Designed for Urdu
        </div>
    """)

# ── Launch ─────────────────────────────────────────────────────────────────────
demo.launch(
    
    show_error=True,
)

