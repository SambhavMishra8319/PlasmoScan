import tensorflow as tf
import cv2
import numpy as np

# Load trained model
model = tf.keras.models.load_model("models/malaria_model.h5")

def predict(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (128, 128))  # Resize to match model input
    image = image / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension

    prediction = model.predict(image)
    if prediction[0][0] > 0.5:
        return "🦠 Uninfected"
    else:
        return "⚠️ Parasitized (Malaria detected)"

# Test with an image
test_image = "data/cell_images/test_sample.png"  # Change to your test image
result = predict(test_image)
print("Prediction:", result)
