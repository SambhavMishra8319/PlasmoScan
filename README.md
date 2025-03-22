PlasmoScan - AI-based Malaria & Anemia Detection

📌 Project Overview

PlasmoScan is an AI-powered diagnostic tool designed to detect malaria and anemia from blood cell images. The model leverages deep learning to classify cell images as Parasitized (Malaria) or Uninfected using a Convolutional Neural Network (CNN).

🚀 Features

Automated Detection: Classifies blood cell images with AI.

Fast & Affordable: Provides quick results for early diagnosis.

Web  Deployment: Accessible through a web app (Flask)
Trained on Large Datasets: Uses labeled blood cell images for accuracy.

📂 Dataset & Preprocessing

Dataset Location: data/cell_images/

Categories: Parasitized/ and Uninfected/

Preprocessing: Images are resized to 128x128, normalized, and saved as NumPy arrays.

Preprocessing Script: preprocess.py

python preprocess.py  # Runs preprocessing on dataset

🏋️ Model Training

Framework: TensorFlow/Keras

Architecture: CNN

Training Script: train_model.py

Trained Model Path: models/malaria_model.h5

python train_model.py  

🌍 Deployment

🔹 Web App (Flask)

File: app.py

Run Locally:

python app.py 

