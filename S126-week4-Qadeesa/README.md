# Urdu OCR Project | Code Saviours SI-26 | Week 4

# What Was Done

## Step 1: Environment Setup
- Installed required libraries (Transformers, Datasets, Evaluate, Accelerate)
- Imported all necessary Python modules
- Loaded the pretrained TrOCR Processor and VisionEncoderDecoderModel

## Step 2: Dataset Preparation
- Loaded the Urdu OCR dataset
- Converted image-text pairs into Hugging Face Dataset format
- Preprocessed images using TrOCRProcessor
- Tokenized Urdu text labels for training

## Step 3: Model Training
- Configured TrainingArguments
- Fine-tuned the TrOCR model using Hugging Face Trainer
- Trained the model on the prepared dataset

## Step 4: Model Evaluation
- Evaluated the model using Character Error Rate (CER)
- Generated predictions on the test dataset
- Compared predicted text with ground truth labels

## Step 5: Results & Saving
- Visualized training loss
- Saved the fine-tuned TrOCR model
- Saved the processor for future OCR inference
