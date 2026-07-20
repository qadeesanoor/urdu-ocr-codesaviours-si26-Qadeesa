# Urdu OCR Project | Code Saviours SI-26 | Week 2
Gap Analysis
Image 1 (urdu_03.png)

Actual: آج موسم بہت اچھا ہے (Aaj mausam bohot acha hai) Tesseract output: آ وک بہت ابچھاے What went wrong: The word "موسم" (mausam) was completely garbled into "وک". The word "اچھا" was misread as "ابچھاے" with extra characters inserted. Connected letters within words were incorrectly split apart.

Image 2 (urdu_08.png)

Actual: سورج مشرق سے طلوع ہوتا ہے (Suraj mashriq se tulu hota hai) Tesseract output: مور مشرمی سے طلو ہوناے What went wrong: "سورج" (sun) was misread entirely as "مور". "مشرق" had its last letter confused, becoming "مشرمی". "طلوع" lost its final letter and became "طلو" — complex letter shapes like ع (ain) were dropped.

Image 3 (urdu_07.png)

Actual: علم حاصل کرنا ہر مسلمان پر فرض ہے Tesseract output: لم حاص لکرا ہر لان بش ہے What went wrong: The first letter "ع" was dropped entirely. Words merged incorrectly across boundaries — "حاصل کرنا" became "حاص لکرا" with the space shifted to the wrong position. Both "مسلمان" and "فرض" came out corrupted.

Image 4 (urdu_10.png)

Actual: محنت کامیابی کی کنجی ہے Tesseract output: نت امب یکی - What went wrong: This was the worst result. The first part of "محنت" ("مح") was dropped completely. "کامیابی" was entirely misread. The output ended in a meaningless dash, meaning the model couldn't recognize the remaining text at all.

Image 5 (urdu_04.png)

Actual: کتاب پڑھنا میرا پسندیدہ مشغلہ ہے Tesseract output: کاب ڑھا مان ہم ہے What went wrong: Nearly half the sentence disappeared entirely — "پسندیدہ مشغلہ" was completely missing from the output. The remaining words were also truncated and shortened.
