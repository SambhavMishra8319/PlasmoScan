import os
import numpy as np
import cv2

INPUT_DIR = "data/cell_images/"
OUTPUT_DIR = "data/processed/"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def preprocess_and_save():
    categories = ["Parasitized", "Uninfected"]
    
    for category in categories:
        img_folder = os.path.join(INPUT_DIR, category)
        save_path = os.path.join(OUTPUT_DIR, f"{category}.npy")

        data = []
        for img_name in os.listdir(img_folder):
            img_path = os.path.join(img_folder, img_name)

            # Skip system files
            if not img_name.lower().endswith((".png", ".jpg", ".jpeg")):
                print(f"Skipping {img_name} (Not an image)")
                continue  

            img = cv2.imread(img_path)
            if img is None:
                print(f"Skipping {img_name} (Unreadable or corrupted)")
                continue  

            img = cv2.resize(img, (128, 128)) / 255.0  # Normalize
            data.append(img)

        if data:
            np.save(save_path, np.array(data))  # Save preprocessed images
            print(f"✅ {category} processed successfully!")
        else:
            print(f"⚠️ No valid images found in {category}!")

preprocess_and_save()
