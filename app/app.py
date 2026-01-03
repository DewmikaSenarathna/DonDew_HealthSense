import streamlit as st
import pickle

# Page configuration
st.set_page_config(
    page_title="DonDew HealthSense",
    page_icon="🩺",
    layout="centered"
)

# Load trained model and vectorizer
@st.cache_resource
def load_model():
    with open("../model/disease_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("../model/tfidf_vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    return model, vectorizer


model, vectorizer = load_model()

# App Title and Description
st.title("🩺 DonDew HealthSense")
st.subheader("AI-Based Disease Symptom Checker")

st.write(
    """
    Enter your symptoms in **simple English**.
    This system uses **Machine Learning** to suggest a possible condition
    based on symptom descriptions.
    """
)

st.divider()

# User Input
user_input = st.text_area(
    "Describe your symptoms:",
    placeholder="Example: I have fever, severe joint pain and skin rashes",
    height=150
)

# Prediction Logic
if st.button("Predict Disease"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter your symptoms before predicting.")
    else:
        # Convert text to numerical vector
        input_vector = vectorizer.transform([user_input])

        # Predict disease
        prediction = model.predict(input_vector)[0]

        # Predict probability
        probabilities = model.predict_proba(input_vector)[0]
        confidence = max(probabilities) * 100

        # Display result
        st.success(f"🧠 Predicted Condition: **{prediction}**")

        st.divider()

        # Disclaimer
        st.warning(
            """
            ⚠️ **Disclaimer**  
            This system is developed **for educational and awareness purposes only**.  
            It does **NOT provide medical diagnosis**.  
            Please consult a **qualified healthcare professional** for medical advice.
            """
        )

# Footer
st.markdown(
    "<center>Developed by <b>Don Dew</b> | DonDew HealthSense</center>",
    unsafe_allow_html=True
)
