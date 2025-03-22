from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
import cv2

app = Flask(__name__)

# Load trained model
MODEL_PATH = "models/malaria_model.h5"  
model = tf.keras.models.load_model(MODEL_PATH)

# Preprocess image
def preprocess_image(image):
    image = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
    image = cv2.resize(image, (128, 128)) / 255.0  # Resize & normalize
    return np.expand_dims(image, axis=0)  

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file uploaded!"
        
        file = request.files["file"]
        image = preprocess_image(file)
        
        prediction = model.predict(image)[0][0]
        result = "Parasitized" if prediction > 0.5 else "Uninfected"

        return render_template("index.html", result=result)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
