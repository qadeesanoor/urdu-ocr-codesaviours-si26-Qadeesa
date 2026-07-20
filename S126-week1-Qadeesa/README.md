# Urdu OCR Project | Code Saviours SI-26 | Week 1
## Project Overview
The goal of this project is to build an **Urdu Optical Character Recognition (OCR)** system that can recognize Urdu text from images and convert it into machine-readable text. During Week 1, the focus was on setting up the development environment, understanding the OCR problem, collecting dataset images, and creating labels for training.

## Research Summary

### What is OCR?
Optical Character Recognition (OCR) is a technology that converts text from images into editable and searchable digital text. OCR enables computers to recognize printed or handwritten characters automatically. It is widely used for digitizing books, documents, receipts, and forms.

### Why is Urdu OCR More Challenging?
Urdu OCR is more difficult than English OCR because Urdu is written from right to left, characters change shape depending on their position in a word, and many letters are connected. Different writing styles, fonts, and image quality also make recognition more challenging.

### Real-World Applications
- Digitizing Urdu books, newspapers, and historical documents.
- Extracting text from Urdu signboards, forms, and official documents for searchable digital records.

---

## Repository Structure

```
urdu-ocr-codesaviours-si26-qadeesa/
│
├── README.md
├── SI26_Week1_Qadeesa.ipynb
│
├── data/
│   ├── labels.csv
│   └── raw/
│       ├── newspaper/
│       ├── books/
│       ├── signboards/

## Dataset
The dataset contains **100+ Urdu text images** collected from different sources, including:
- Public Urdu OCR datasets
- Books and newspapers
- Signboards
- Synthetic Urdu text images generated in Google Colab
Each image is paired with its correct text transcription in **labels.csv**.
---
## Technologies Used

- Python
- Google Colab
- Pillow (PIL)
- Arabic Reshaper
- Python Bidi
- CSV
- GitHub
- Hugging Face

