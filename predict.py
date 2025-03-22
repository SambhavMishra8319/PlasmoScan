import tensorflow as tf
import cv2
import numpy as np


model = tf.keras.models.load_model("models/malaria_model.h5")

def predict(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (128, 128))  
    image = image / 255.0 
    image = np.expand_dims(image, axis=0) 

    prediction = model.predict(image)
    if prediction[0][0] > 0.5:
        return "🦠 Uninfected"
    else:
        return "⚠️ Parasitized (Malaria detected)"


test_image = "data/cell_images/test_sample.png"  
result = predict(test_image)
print("Prediction:", result)
