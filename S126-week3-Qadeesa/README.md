Urdu OCR Project - Week 3
Programme

ML / AI Internship - SI-26 Code Saviours (SMC-PRIVATE) Limited

Week 3 Goal

Expand the dataset to 200+ images and build a PyTorch Dataset class for model training.

What Was Done

Step 1: Dataset Expansion
Expanded image collection from 100 (Week 1) to 200+ images
Added variety in fonts, backgrounds, and text sizes
Updated data/labels.csv with new entries
Ran Week 2 preprocessing script on all new images
Step 2: Dataset Class
Built UrduOCRDataset, a PyTorch Dataset subclass
Implements __len__ and __getitem__
Loads each image, processes it using TrOCRProcessor, and returns paired pixel values and tokenized text labels
Step 3: Testing
Verified dataset loads correctly by checking sample shapes
Created an 80/20 train/test split using torch.utils.data.random_split
Built DataLoader objects for both splits and confirmed batch loading works

Files
File	                Description
Week3_Urdu_OCR.ipynb	Notebook containing dataset expansion check, Dataset class, and DataLoader setup
data/labels.csv	      Updated labels file with 200+ image-text pairs
data/processed/	      Preprocessed images from Week 2 pipeline
