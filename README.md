🩺 DonDew HealthSense
AI-Based Disease Symptom Checker using Machine Learning & NLP
📌 Project Overview

DonDew HealthSense is a software-only Machine Learning project that predicts possible diseases based on user-described symptoms written in natural English.
The system uses Natural Language Processing (NLP) techniques and classification models to analyze symptom text and suggest a likely condition with a confidence score.

This project is developed for educational and health-awareness purposes only and does not replace professional medical diagnosis.

🎯 Problem Statement

Many people struggle to understand what their symptoms might indicate, especially when access to immediate medical guidance is limited.
This project aims to demonstrate how Machine Learning and NLP can be used to build an early symptom-based awareness system that supports informed decision-making.

🧠 Solution Approach

The system follows a complete ML pipeline:

User enters symptoms in natural English

Text is cleaned and normalized

Symptoms are converted into numerical features using TF-IDF

A trained ML model predicts the most likely disease

The system displays:

Predicted condition

Confidence score

Ethical disclaimer

🛠️ Technologies Used

Python

Scikit-learn

Pandas & NumPy

TF-IDF Vectorization

Logistic Regression

Streamlit (Web Interface)

Git & GitHub

📂 Project Structure
DonDew_HealthSense/
│
├── app/
│   └── app.py                 # Streamlit web application
│
├── model/
│   ├── disease_model.pkl      # Trained ML model
│   └── tfidf_vectorizer.pkl   # Text vectorizer
│
├── notebooks/
│   └── model_training.ipynb   # Model training notebook
│
├── data/
│   └── disease_symptoms.csv   # Dataset
│
└── README.md

🧪 Machine Learning Details

Problem Type: Multi-class text classification

Input: Symptom descriptions (text)

Output: Predicted disease label

Model: Logistic Regression (class-balanced)

Feature Extraction: TF-IDF with uni-grams and bi-grams

Text preprocessing and synonym normalization are applied to improve real-world prediction accuracy.

🌐 Web Application

A simple and user-friendly Streamlit web interface allows users to:

Enter symptoms in plain English

Receive a predicted condition

View prediction confidence

This interface demonstrates how ML models can be integrated into real applications.

⚠️ Disclaimer

This system is developed for educational and awareness purposes only.
It does NOT provide medical diagnosis.
Users should consult a qualified healthcare professional for medical advice.

🚀 How to Run the Project
# Navigate to app directory
cd DonDew_HealthSense/app

# Run Streamlit app
streamlit run app.py

📈 Future Improvements

Top-3 disease predictions

Multilingual support (Sinhala / Tamil)

Online deployment (Streamlit Cloud)

Improved symptom synonym coverage

👤 Author

Don Dew
Machine Learning & Software Engineering Enthusiast
