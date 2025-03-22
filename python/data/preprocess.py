import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Paths
DATASET_PATH = "cell_images"  
PROCESSED_PATH = "processed_data"
IMG_SIZE = 128

# Create processed data directory
if not os.path.exists(PROCESSED_PATH):
    os.makedirs(f"{PROCESSED_PATH}/Parasitized")
    os.makedirs(f"{PROCESSED_PATH}/Uninfected")

# Function to preprocess images
def preprocess_and_save(folder):
    for label in ["Parasitized", "Uninfected"]:
        img_folder = os.path.join(DATASET_PATH, label)
        save_folder = os.path.join(PROCESSED_PATH, label)
        
        for img_name in os.listdir(img_folder):
            img_path = os.path.join(img_folder, img_name)
            img = cv2.imread(img_path)
            if img is not None:
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))  
                img = img / 255.0  
                # Save processed image
                save_path = os.path.join(save_folder, img_name)
                cv2.imwrite(save_path, (img * 255).astype(np.uint8))

# Run preprocessing
preprocess_and_save(DATASET_PATH)
print("✅ Preprocessing complete! Processed images saved in 'processed_data/'")
