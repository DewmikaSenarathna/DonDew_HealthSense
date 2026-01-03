# 🩺 DonDew HealthSense  
## AI-Based Disease Symptom Checker using Machine Learning & NLP

---

## 📌 Project Overview

**DonDew HealthSense** is a software-only Machine Learning application that predicts possible diseases based on symptom descriptions written in natural English.  
The system uses **Natural Language Processing (NLP)** and **Machine Learning classification models** to analyze user-input text and suggest a likely condition along with a confidence score.

This project is designed strictly for **educational and health-awareness purposes** and does **not** replace professional medical diagnosis.

---

## 🎯 Problem Statement

Many individuals experience symptoms but struggle to understand what those symptoms might indicate, especially when immediate access to medical professionals is limited.  
This project demonstrates how **Machine Learning and NLP** can be used to build a **symptom-based awareness system** that provides preliminary insights and encourages informed decision-making.

---

## 🧠 Solution Approach

The system follows a complete and structured Machine Learning workflow:

1. The user enters symptoms in natural English  
2. The text input is cleaned and normalized  
3. Symptoms are converted into numerical features using **TF-IDF vectorization**  
4. A trained ML model predicts the most likely disease  
5. The system displays:
   - Predicted condition  
   - Prediction confidence  
   - Ethical disclaimer  

This approach ensures clarity, responsibility, and usability.

---

## 🛠️ Technologies Used

- **Python**
- **Scikit-learn**
- **Pandas & NumPy**
- **Natural Language Processing (NLP)**
- **TF-IDF Vectorization**
- **Logistic Regression**
- **Streamlit** (Web Interface)
- **Git & GitHub**

---

## 📂 Project Structure

DonDew_HealthSense/
│
├── app/
│ └── app.py # Streamlit web application
│
├── model/
│ ├── disease_model.pkl # Trained ML model
│ └── tfidf_vectorizer.pkl # TF-IDF vectorizer
│
├── notebooks/
│ └── model_training.ipynb # Model training and evaluation
│
├── data/
│ └── disease_symptoms.csv # Dataset
│
└── README.md


---

## 🧪 Machine Learning Details

- **Problem Type:** Multi-class text classification  
- **Input:** Symptom descriptions (text)  
- **Output:** Predicted disease label  
- **Model Used:** Logistic Regression (class-balanced)  
- **Feature Extraction:** TF-IDF with uni-grams and bi-grams  

Text preprocessing and synonym normalization are applied to improve real-world prediction performance.

---

## 🌐 Web Application

A simple and user-friendly **Streamlit web interface** allows users to:

- Enter symptoms in plain English  
- Receive a predicted disease  
- View the prediction confidence  

This demonstrates how a trained ML model can be integrated into a real-world software application.

---

## ⚠️ Disclaimer

> **Disclaimer:**  
> This system is developed **for educational and health-awareness purposes only**.  
> It does **NOT provide medical diagnosis**.  
> Users should consult a **qualified healthcare professional** for medical advice.

---

## 🚀 How to Run the Project

### 1️⃣ Install Required Libraries

```bash
pip install streamlit scikit-learn pandas numpy

2️⃣ Run the Streamlit Application
cd DonDew_HealthSense/app
streamlit run app.py


The application will open automatically in your default web browser.