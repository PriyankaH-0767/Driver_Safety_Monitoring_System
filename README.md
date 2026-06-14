# Driver Safety Monitoring System using Teachable Machine

## Project Overview

The Driver Safety Monitoring System is an image recognition project developed using Google Teachable Machine and Python. The system classifies the driver's condition into one of the following categories:

* Active Driver
* Distracted Driver
* Sleeping (Drowsy) Driver

The primary objective of this project is to improve road safety by detecting unsafe driving behaviour in real time.

---

## Problem Statement

Driver fatigue and distraction are among the major causes of road accidents. Continuous monitoring of a driver's state can help in identifying risky situations and preventing accidents.

This project uses a machine learning model trained with Teachable Machine to recognize different driver states through image classification.

---

## Objectives

* Detect whether the driver is active, distracted, or sleeping.
* Use image recognition techniques for classification.
* Provide a simple and user-friendly driver monitoring solution.
* Demonstrate the practical application of machine learning in road safety.

---

## Technologies Used

* Google Teachable Machine
* Python
* TensorFlow / Keras
* OpenCV
* NumPy
* Pillow

---

## Dataset Classes

The model was trained using three classes:

1. Active Driver
2. Distracted Driver
3. Sleeping Driver

---

## Project Structure

Driver-Safety-Monitoring-System/

├── app.py

├── keras_model.h5

├── labels.txt

├── requirements.txt

├── README.md

└── screenshots/

---

## How to Run the Project

### 1. Clone the Repository

git clone 

### 2. Navigate to the Project Folder

cd Driver-Safety-Monitoring-System

### 3. Install Required Libraries

pip install -r requirements.txt

### 4. Run the Application

python app.py

### 5. Usage

* The webcam will open automatically.
* The system captures frames from the webcam.
* The trained model predicts the driver's state.
* The prediction result and confidence score are displayed on the screen.
* Press 'q' to exit the application.

---

## Results

The system successfully classifies the driver's condition into:

* Active
* Distracted
* Sleeping

based on the trained Teachable Machine model.

---

## Future Enhancements

* Add an alarm system when drowsiness is detected.
* Store detection logs for analysis.
* Deploy the system on embedded devices such as Raspberry Pi.
* Integrate GPS and emergency notification features.
* Develop a mobile application interface.

---

## Conclusion

The Driver Safety Monitoring System demonstrates how machine learning and image recognition can be used to improve road safety. By identifying driver distraction and drowsiness in real time, the system has the potential to reduce accidents and promote safer driving practices.

---

## Author

Priyanka H

Mini Project
