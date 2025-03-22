PlasmoScan - AI-based Malaria Detection

🏥 What PlasmoScan Does

PlasmoScan is an AI-powered web application designed to detect malaria from blood smear images. It utilizes deep learning to analyze cell images and provide a prediction on whether malaria is present. The goal is to provide an affordable and accessible diagnostic tool for early malaria detection.

🔧 How to Run It

1️⃣ Installation

Ensure you have Python installed, then clone this repository:

git clone https://github.com/yourusername/PlasmoScan.git
cd PlasmoScan

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Web Application

python app.py

The app will run on http://127.0.0.1:5000/.

📸 Dataset Location

The dataset is located at data/cell_images/. Due to its large size, you can download it from:
Dataset Link

🖼️ Flowchart of the System

User Uploads Blood Smear Image 📤

AI Analyzes Image Using Deep Learning Model 🤖

Prediction with Confidence Score is Generated 📊

Result is Displayed to the User ✅

💡 Challenges We Ran Into

Training the model with a high accuracy while avoiding overfitting.

Optimizing image preprocessing to improve prediction quality.

Implementing a smooth and user-friendly web interface.

Handling large dataset files and managing deployment.

🔬 Technologies Used

Deep Learning: TensorFlow/Keras

Computer Vision: OpenCV

Backend: Flask/Django

Frontend: HTML, CSS, JavaScript

Mobile App (Future Expansion): Flutter
