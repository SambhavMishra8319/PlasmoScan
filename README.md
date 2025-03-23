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

Use Case: How PlasmoScan Works in a Real-Life Scenario
Patient Visits a Local Clinic

A patient in a rural area shows symptoms like fever, chills, and fatigue.

The local healthcare worker suspects malaria and decides to test for it.

Blood Sample Collection

A small blood sample is taken from the patient.

The sample is prepared as a blood smear on a glass slide.

Microscopic Image Capture

The slide is placed under a microscope.

The healthcare worker captures an image using a mobile camera or digital microscope.

Image Upload to PlasmoScan

The captured image is uploaded to PlasmoScan via a mobile or web-based interface.

AI-Powered Analysis

PlasmoScan processes the image using deep learning algorithms.

It detects malaria parasites and calculates the confidence score.

Instant Diagnosis Result

The system provides an immediate result:

Positive for Malaria → The patient is advised to begin treatment.

Negative for Malaria → Further medical evaluation may be needed.

Faster Treatment & Improved Healthcare

The healthcare worker prescribes the necessary treatment.

The patient receives timely care, reducing complications and risk of severe malaria.

This process eliminates delays, reduces dependence on expert technicians, and brings affordable malaria detection to remote areas.
