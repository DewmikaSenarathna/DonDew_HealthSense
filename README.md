```markdown
# 🩺 DonDew HealthSense  
### AI-Based Disease Symptom Checker using Machine Learning & NLP

---

## 📖 Overview

**DonDew HealthSense** is an end-to-end **Machine Learning and Natural Language Processing (NLP)** project that predicts possible disease categories based on symptom descriptions written in natural English.

The system is designed as a **software-only, awareness-level healthcare application** that demonstrates how text-based ML classification models can be applied responsibly in medical-related domains.

> ⚠️ This project is strictly for **educational and health-awareness purposes** and does **not** replace professional medical diagnosis.

---

## 🎯 Problem Statement

People often experience symptoms but lack immediate access to medical professionals. Searching symptoms online frequently results in misleading or fragmented information.

This project addresses that problem by:
- Structuring symptom interpretation using NLP
- Applying supervised Machine Learning instead of keyword matching
- Presenting results with transparency and ethical safeguards

---

## 💡 Solution Approach

DonDew HealthSense follows a **standard Machine Learning workflow**:

1. User inputs symptoms in natural English  
2. Text is cleaned and normalized  
3. Symptoms are converted into numerical vectors using **TF-IDF**  
4. A trained **Logistic Regression** classifier predicts the disease  
5. The system displays:
   - Predicted disease category  
   - Prediction confidence score  
   - Medical disclaimer  

This ensures interpretability, reproducibility, and responsible usage.

---

## 🧠 Machine Learning Details

| Aspect | Description |
|------|-------------|
| Problem Type | Multi-class text classification |
| Input | Symptom descriptions (free text) |
| Output | Disease category |
| Feature Engineering | TF-IDF (uni-grams & bi-grams) |
| Model | Logistic Regression (class-balanced) |
| Evaluation | Accuracy & classification report |

---

## 🛠️ Technology Stack

- Python  
- Scikit-learn  
- Pandas & NumPy  
- Natural Language Processing (NLP)  
- TF-IDF Vectorization  
- Logistic Regression  
- Streamlit (Web Interface)  
- Git & GitHub  

---

## 📁 Project Structure

```

DonDew_HealthSense/
│
├── app/
│   └── app.py                 # Streamlit web application
│
├── model/
│   ├── disease_model.pkl      # Trained ML model
│   └── tfidf_vectorizer.pkl   # Saved TF-IDF vectorizer
│
├── data/
│   └── disease_symptoms.csv   # Dataset
│
├── notebooks/
│   └── model_training.py      # Model training script
│
└── README.md

````

---

## 🌐 Web Application Features

- Simple and intuitive user interface  
- Free-text symptom input  
- Real-time disease prediction  
- Confidence score display  
- Ethical and medical disclaimer  

---

## ⚠️ Disclaimer

> **Important Notice**  
> This system is developed **only for educational and health-awareness purposes**.  
> It **does NOT provide medical diagnosis or treatment advice**.  
> Always consult a **qualified healthcare professional** for medical concerns.

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/DonDew_HealthSense.git
cd DonDew_HealthSense
````

### 2️⃣ Install Dependencies

```bash
pip install streamlit scikit-learn pandas numpy
```

### 3️⃣ Train the Model

```bash
python notebooks/model_training.py
```

### 4️⃣ Run the Streamlit Application

```bash
cd app
streamlit run app.py
```

The application will open automatically in your default web browser.

---

## 📈 Future Enhancements

* Deep Learning models (LSTM / BERT)
* Multilingual symptom support
* Explainable AI (SHAP / LIME)
* Mobile application integration
* Expanded and real-world datasets

---

## 👨‍💻 Author

**Don Dew**
Computer Engineering Undergraduate
Machine Learning | NLP | Software Engineering

---

## ⭐ Acknowledgement

This project was developed as part of academic self-learning to demonstrate practical applications of **Machine Learning and NLP in healthcare awareness systems**.

```
```
