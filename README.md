PlasmoScan - AI-based Malaria Detection
🏥 What is PlasmoScan?
PlasmoScan is an AI-powered web application designed to detect malaria from blood smear images. It leverages deep learning techniques to analyze cell images and predict whether malaria is present. The goal is to provide an affordable and accessible diagnostic tool, particularly for rural and underserved communities, enabling early detection and timely treatment of malaria.



📸 Dataset Location
The dataset used for training and testing is stored at:
data/cell_images/

📌 Due to its large size, you can download the dataset from:
🔗 Dataset Link https://lhncbc.nlm.nih.gov/publication/pub9932

🖼️ Flowchart of the System
Below is the workflow of PlasmoScan from image upload to diagnosis result:

1️⃣ User Uploads a Blood Smear Image 📤
2️⃣ AI Analyzes the Image Using Deep Learning 🤖
3️⃣ Prediction with Confidence Score is Generated 📊
4️⃣ Result is Displayed to the User ✅

<img width="941" alt="flow chart" src="https://github.com/user-attachments/assets/8a763977-f7ef-44ce-9155-29928f021b28" />

💡 Challenges We Faced
During the development of PlasmoScan, we encountered several challenges, including:

Model Accuracy & Overfitting: Ensuring high prediction accuracy while preventing overfitting during training.

Image Preprocessing: Optimizing techniques like noise reduction and feature extraction to improve detection quality.

User Interface: Designing a simple and intuitive interface for easy usability by non-technical users.

Dataset Handling: Managing large dataset files efficiently while ensuring smooth AI model training and testing.

Deployment: Making the AI model lightweight and fast for real-time predictions.

🔬 Technologies Used
Category	Technologies
Deep Learning	TensorFlow, Keras
Computer Vision	OpenCV
Backend	Flask, Django
Frontend	HTML, CSS, JavaScript
Mobile App (Future Expansion)	Flutter
🌍 Use Case: How PlasmoScan Works in a Real-Life Scenario
Step 1: Patient Visits a Local Clinic
A patient in a rural area experiences symptoms such as fever, chills, and fatigue.

The healthcare worker suspects malaria and decides to conduct a diagnostic test.

Step 2: Blood Sample Collection
A small blood sample is taken from the patient.

The sample is prepared as a blood smear on a glass slide.

Step 3: Microscopic Image Capture
The prepared slide is placed under a microscope.

The healthcare worker captures an image using a mobile camera or digital microscope.

Step 4: Image Upload to PlasmoScan
The captured image is uploaded to PlasmoScan through a mobile or web-based interface.

Step 5: AI-Powered Analysis
The uploaded image is processed using a deep learning model trained on malaria detection.

The AI detects malaria parasites and calculates a confidence score.

Step 6: Instant Diagnosis Result
The system provides an immediate diagnostic result:
✅ Positive for Malaria → The patient is advised to begin treatment immediately.
❌ Negative for Malaria → Further medical evaluation may be needed.

Step 7: Faster Treatment & Improved Healthcare
The healthcare worker prescribes treatment without waiting for centralized lab results.

The patient receives timely care, reducing complications and risk of severe malaria.

📌 This process eliminates delays, reduces dependence on expert technicians, and makes malaria detection affordable for rural healthcare systems.

📢 Future Scope
🚀 PlasmoScan aims to expand with additional features:

Mobile App Integration: Allowing direct image upload via mobile phones.

Multi-Disease Detection: Extending the model to detect anemia and other blood-related conditions.

Cloud-Based AI Processing: To enable real-time processing and result retrieval.

Integration with Health Organizations: Partnering with NGOs and healthcare providers for large-scale deployment.

🏆 Contributors & Team Members
👨‍💻 Sambhav Mishra (Lead Developer, AI Engineer)
👩‍💻 Vansh Talani (Frontend & Backend Development)
📊 Sundaram  (Data Science & Model Training)

📩 Contact & Support
📧 Email:sammishr8319@gmail.com
🌐 Project Repository: [GitHub Repo](https://github.com/SambhavMishra8319/PlasmoScan/)

🚀 Join us in revolutionizing malaria detection with AI!

