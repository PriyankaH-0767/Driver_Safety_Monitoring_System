# Driver Safety Monitoring System using Google Teachable Machine

## Project Overview

The Driver Safety Monitoring System is an image classification project developed using Google Teachable Machine. The project aims to identify the driver's condition and classify it into one of three categories:

* Active Driver
* Distracted Driver
* Sleeping (Drowsy) Driver

The objective of this project is to demonstrate how machine learning can be used to monitor driver behaviour and improve road safety.

---

## Problem Statement

Driver distraction and drowsiness are major causes of road accidents. Detecting unsafe driving conditions at an early stage can help reduce the risk of accidents and promote safer driving practices.

This project uses image recognition to classify a driver's state based on webcam input.

---

## Objectives

* Train an image classification model using Google Teachable Machine.
* Classify the driver's condition into Active, Distracted, and Sleeping categories.
* Demonstrate the effectiveness of machine learning in driver safety applications.
* Provide a simple and accessible solution without requiring complex deployment.

---

## Technologies Used

* Google Teachable Machine
* TensorFlow (Keras Export)
* Image Classification
* Webcam-based Testing

---

## Dataset Classes

The model was trained using the following three classes:

1. Active Driver
2. Distracted Driver
3. Sleeping Driver

---

## Model Export

The trained model was exported from Google Teachable Machine using:

TensorFlow → Keras Export

Exported Files:

* keras_model.h5
* labels.txt

---

## Testing Method

The model was tested using the built-in webcam preview available in Google Teachable Machine.

The webcam captured live images and classified the driver's condition in real time.

---

## Project Structure

Driver-Safety-Monitoring-System/

├── keras_model.h5

├── labels.txt

├── README.md

└── screenshots/

---

## Results

The trained model successfully identified and classified the driver's condition into:

* Active Driver
* Distracted Driver
* Sleeping Driver

Screenshots of the model predictions obtained from the Teachable Machine webcam preview are included in the repository.

---

## Future Enhancements

* Develop a standalone Python application for real-time monitoring.
* Integrate an alarm system for drowsiness detection.
* Deploy the model on embedded systems such as Raspberry Pi.
* Add logging and alert features.
* Extend the system with additional driver behaviour classes.

---

## Conclusion

This project demonstrates the practical application of machine learning and image recognition in the field of driver safety. Using Google Teachable Machine, an effective image classification model was developed to detect driver alertness and distraction through webcam-based testing.

---

## Author

Priyanka H
Mini trial project



