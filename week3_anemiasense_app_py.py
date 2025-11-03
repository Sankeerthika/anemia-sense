# ------------------------------------------------------
# Week3_AnemiaSense_App.py
# ------------------------------------------------------
# Streamlit App for Anemia Prediction
# ------------------------------------------------------

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# App title
st.title("🩸 AnemiaSense - Anemia Detection using Machine Learning")
st.write("Enter your details below to check if you may have anemia.")

# User Inputs
gender = st.selectbox("Gender", ("Male", "Female"))
hemoglobin = st.number_input("Hemoglobin (g/dL)", min_value=0.0, max_value=20.0, value=13.5)
mch = st.number_input("MCH", min_value=0.0, max_value=50.0, value=25.0)
mchc = st.number_input("MCHC", min_value=0.0, max_value=50.0, value=30.0)
mcv = st.number_input("MCV", min_value=0.0, max_value=120.0, value=80.0)

# Convert Gender to numeric
gender_num = 1 if gender == "Male" else 0

# Create input DataFrame
input_data = pd.DataFrame({
    "Gender": [gender_num],
    "Hemoglobin": [hemoglobin],
    "MCH": [mch],
    "MCHC": [mchc],
    "MCV": [mcv]
})

# Predict Button
if st.button("🔍 Predict Anemia Status"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("🔴 The person is **Anemic**. Please consult a healthcare professional.")
    else:
        st.success("🟢 The person is **Not Anemic**.")
