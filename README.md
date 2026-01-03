# 🩺 DonDew HealthSense  
### AI-Based Disease Symptom Checker using Machine Learning & NLP

---
<br>

## 📌 Project Overview

**DonDew HealthSense** is a software-only Machine Learning application designed to predict potential diseases based on symptoms described by users in natural English.  
The system leverages **Natural Language Processing (NLP)** techniques and supervised **Machine Learning classification models** to analyze free-text symptom inputs and return a probable medical condition along with a confidence score.

This project is developed **strictly for educational and health-awareness purposes** and **does not replace professional medical diagnosis or treatment**.

---
<br>

## 🎯 Problem Statement

In many real-world scenarios, individuals experience symptoms but lack immediate access to reliable medical guidance. This often leads to confusion, misinformation, or delayed action.

The objective of this project is to demonstrate how **Machine Learning and NLP** can be applied to create an **early-stage symptom awareness system** that:
- Interprets unstructured symptom descriptions
- Provides preliminary insights
- Encourages informed and responsible decision-making

---
<br>

## 🧠 Solution Approach

The system follows a structured and end-to-end Machine Learning pipeline:

1. Users enter symptoms in **natural English language**
2. Input text is **cleaned, normalized, and preprocessed**
3. Symptoms are transformed into numerical features using **TF-IDF vectorization**
4. A trained **Machine Learning classification model** predicts the most likely disease
5. The system outputs:
   - Predicted condition
   - Confidence score
   - Ethical and medical disclaimer

---
<br>

## 🛠️ Technologies Used

- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn  
- **Data Handling:** Pandas, NumPy  
- **Feature Extraction:** TF-IDF Vectorization  
- **Model:** Logistic Regression (Class-balanced)  
- **Web Interface:** Streamlit  
- **Version Control:** Git & GitHub  

---
<br>

## 📂 Project Structure

```text
DonDew_HealthSense/
│
├── app/
│   └── app.py                  # Streamlit web application
│
├── model/
│   ├── disease_model.pkl       # Trained ML classification model
│   └── tfidf_vectorizer.pkl    # TF-IDF vectorizer
│
├── notebooks/
│   └── model_training.ipynb    # Model training and evaluation
│
├── data/
│   └── disease_symptoms.csv    # Dataset used for training
│
└── README.md
```
---
<br>



## 🧪 Machine Learning Details

- **Problem Type:** Multi-class text classification  
- **Input:** Free-text symptom descriptions provided by users  
- **Output:** Predicted disease label  

### Model
- **Algorithm:** Logistic Regression  
- **Class Handling:** Class-balanced training to address data imbalance  

### Feature Engineering
- TF-IDF vectorization  
- Uni-gram and bi-gram feature extraction  

### Text Preprocessing
- Text cleaning (noise removal and formatting)  
- Text normalization  
- Symptom synonym handling to improve robustness and real-world accuracy  

---
<br>

## 🌐 Web Application

The project includes a clean, lightweight, and user-friendly **Streamlit-based web interface** that allows users to:

- Enter symptom descriptions in plain English  
- Receive a predicted medical condition  
- View the model’s confidence score  
- Understand the ethical scope and limitations of the system  

This interface demonstrates how Machine Learning models can be effectively **integrated into real-world applications** for practical use and awareness.

---
<br>

## ⚠️ Disclaimer

This system is developed **strictly for educational and health-awareness purposes**.  
It **does not provide medical diagnosis or treatment recommendations**.

Users are strongly advised to consult a **qualified healthcare professional** for any medical concerns or decisions.

---
<br>

## 🚀 How to Run the Project

```bash
# Navigate to the application directory
cd DonDew_HealthSense/app

# Run the Streamlit application
streamlit run app.py
