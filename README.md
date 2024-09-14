# Face Recognition Antispoofing Deep Learning Model

## Overview
This project implements a **Face Recognition Antispoofing Deep Learning Model** based on the **VGG16** architecture. The model is designed to differentiate between real(Liveness) and fake faces in order to prevent spoofing attacks during facial recognition. Below is a step-by-step description of the process, from data preparation to model training.

## Dataset Preparation
1. **Data Collection**: The dataset consists of both real and fake face images. The data was shuffled before being processed.
   
2. **Data Cleaning**: 
   - I  separated real and fake images into two distinct categories By using python script.
   - Irrelevant data was removed, ensuring that only valid and useful images were retained for training.
   - The data was further cleaned to eliminate noise and artifacts.

## Data Preprocessing
To prepare the data for training, the following preprocessing steps were applied:
1. **Resizing Images**: All images were resized to match the input dimensions required by the VGG16 model (224x224 pixels).
2. **Normalization**: Pixel values were normalized to range between 0 and 1 to improve training performance.
3. **Augmentation**: Random transformations (e.g., flipping, rotating) were applied to increase the variety of the dataset, reducing overfitting.


## Model Architecture
The model architecture is based on the pre-trained **VGG16** network, which was fine-tuned to accommodate the specific needs of the face antispoofing task.
- **Base Model**: VGG16 was used for feature extraction, with the top layers removed.
- **Custom Layers**: Two additional layers were added to the pre-trained model:
  - A **fully connected layer** with 64 units and ReLU activation.
  - A **sigmoid layer** for binary classification (real vs. fake).
- The custom layers help the model learn specific patterns related to real and spoofed faces.

## Training
The model was trained using the cleaned and preprocessed dataset, with the following configurations:
- **Optimizer**: Adam optimizer .
- **Loss Function**: Binary cross-entropy, suitable for a two-class classification problem.
- **Training**: The model was trained for 50 epochs with early stopping applied to prevent overfitting.

## Results
After training, the model achieved an accuracy of **98%** on the test dataset, demonstrating its effectiveness in distinguishing real faces from spoofed ones.

## Download the Model
You can download the trained model directly from this repository and use it for your own face recognition antispoofing tasks:
- [Download Model](Model)

## Conclusion
This project successfully builds an antispoofing deep learning model based on VGG16 with 98% accuracy. It is capable of detecting real(Liveness) and fake faces, contributing to more secure facial recognition systems.
