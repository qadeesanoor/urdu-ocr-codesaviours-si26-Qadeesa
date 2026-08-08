#  **Urdu OCR using TrOCR | Code Saviours SI-26 | Qadeesanoor**
An end-to-end **Urdu Optical Character Recognition (OCR)** project developed during the **Code Saviours SI-26 Internship**. This repository documents the complete development process over **4 weeks**, from dataset preparation to training and evaluating a deep learning OCR model.

## ** Project Overview**
Urdu OCR is a computer vision and deep learning project that converts printed Urdu text from images into editable digital text.
This project uses Microsoft's **TrOCR (Transformer-based OCR)** architecture from Hugging Face to recognize Urdu text from scanned images and documents.
The repository is divided into weekly milestones to demonstrate the complete development workflow.

##** Objectives**
- Build an OCR system for printed Urdu text.
- Prepare and clean an Urdu OCR dataset.
- Fine-tune a Transformer-based OCR model.
- Evaluate recognition performance.
- Document the entire machine learning pipeline.

## **Gap Analysis**
| Area                | Current State                    | Desired State                        | Gap                          | Recommendation                                                  |
| ------------------- | -------------------------------- | ------------------------------------ | ---------------------------- | --------------------------------------------------------------- |
| Dataset             | Limited printed Urdu images      | Large, diverse dataset               | Need more data               | Collect more images from books, newspapers, and documents       |
| Image Quality       | Mixed image quality              | High-quality, noise-free images      | Some images are blurry/noisy | Apply preprocessing (denoising, resizing, contrast enhancement) |
| Model               | TrOCR fine-tuned on limited data | High-accuracy OCR model              | Accuracy can improve         | Train on larger dataset and tune hyperparameters                |
| Evaluation          | Basic testing                    | Comprehensive evaluation             | Few evaluation metrics       | Add CER (Character Error Rate), WER (Word Error Rate), Accuracy |
| Generalization      | Works on printed text            | Works on different fonts and layouts | Limited font diversity       | Include multiple Urdu fonts and document styles                 |
| Handwritten Support | Not supported                    | Recognize handwritten Urdu           | Missing feature              | Train on handwritten Urdu datasets                              |
| Deployment          | Runs in notebook                 | Web or mobile application            | No deployment                | Deploy using Flask, FastAPI, or Streamlit                       |
| User Interface      | Command-line/Notebook            | User-friendly interface              | No GUI                       | Build a web interface for image upload and OCR                  |

##  **Project Timeline**

## ** Week 1 — Data Collection & Preparation**
### **Tasks Completed**
- Repository setup
- Dataset collection
- Folder organization
- Image preprocessing
- Label creation
###** Why Urdu OCR is Challenging**
Developing OCR for Urdu is considerably more difficult than English because of several language-specific characteristics.
**Connected Script**
Urdu letters join together within words, making segmentation significantly harder.
**Variable Character Shapes**
Each Urdu character may appear differently depending on whether it occurs at the beginning, middle, end, or alone.
**Right-to-Left Writing**
Unlike English, Urdu is written from right to left, requiring specialized processing pipelines.
**Limited Training Data**
Publicly available Urdu OCR datasets are much smaller than those available for English, making model training more challenging.
**Nastaliq Layout**
Most printed Urdu uses the Nastaliq writing style, where characters overlap vertically and diagonally, increasing recognition difficulty.

## **Week 2 — Data Preprocessing**
###** Tasks Completed**
- Image resizing
- Image normalization
- Dataset loading
- Train/Validation split
- Data inspection
- Data augmentation (if applicable)
### **Processed Dataset**
The preprocessing pipeline generated a new directory while preserving the original raw dataset.
data/
├── raw/
└── processed/
Keeping both versions allows experiments using either the original or processed images.
### **Why Did Tesseract Fail?**
Several fundamental characteristics of Urdu make it difficult for traditional OCR systems.
**Connected Writing Style**
Urdu characters connect together, making segmentation much more difficult than Latin-based languages.
**Multiple Character Forms**
Individual letters change appearance depending on their location inside a word.
**Nastaliq Script**
The slanted Nastaliq writing style introduces overlapping characters and diagonal arrangements that standard OCR engines struggle to interpret.
**Limited Urdu Optimization**
Most publicly available OCR engines are trained primarily on English and other Latin scripts.
As a result, Urdu receives significantly lower recognition accuracy.

## Week 3 — Model Training
### Tasks Completed
- Load Microsoft TrOCR model
- Configure processor
- Create PyTorch Dataset
- Fine-tune model
- Save checkpoints
- Monitor training loss
### Model Used
- Microsoft TrOCR
- Vision Encoder Decoder
- Hugging Face Transformers
## Week 4 — Evaluation & Testing
### Tasks Completed
- Load trained model
- OCR inference
- Prediction visualization
- Model evaluation
- Error analysis
- Final testing
