# ------------------------------------------------------
# Week3_AnemiaSense_App.py
# ------------------------------------------------------
# Streamlit App for Anemia Prediction
# ------------------------------------------------------

import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load Model
model = joblib.load("model.pkl")

st.title("🩸 AnemiaSense - Anemia Detection Using ML")
st.write("Enter the values below to check your anemia status.")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
hb = st.number_input("Hemoglobin (g/dL)", min_value=1.0, max_value=20.0, value=13.5)
mch = st.number_input("MCH", min_value=1.0, max_value=40.0, value=25.0)
mchc = st.number_input("MCHC", min_value=15.0, max_value=40.0, value=30.0)
mcv = st.number_input("MCV", min_value=50.0, max_value=120.0, value=80.0)

# Button
if st.button("Check Anemia Status"):
    
    # Convert gender to numeric
    gender_num = 0 if gender == "Male" else 1
    
    # Prediction
    input_data = np.array([[gender_num, hb, mch, mchc, mcv]])
    prediction = model.predict(input_data)[0]

    # ✅ Determine Risk Levels
    if (gender == "Male" and hb < 13) or (gender == "Female" and hb < 12):
        risk_level = "High"
    elif (gender == "Male" and 13 <= hb < 13.5) or (gender == "Female" and 12 <= hb < 12.5):
        risk_level = "Moderate"
    else:
        risk_level = "Normal"

    # ✅ Output Message
    if prediction == 1:
        st.error(f"🔴 Result: The person is ANEMIC.\n⚠ Risk Level: **{risk_level}**")
    else:
        st.success(f"🟢 Result: The person is NOT anemic.\n✅ Risk Level: **Normal**")

    # ✅ Diet Suggestions
    if prediction == 1:
        st.subheader("🍎 Suggested Diet for Anemia")
        st.write("""
        ✅ Iron-rich foods: Spinach, beetroot, eggs, meat, fish  
        ✅ Vitamin C foods: Lemon, orange, tomatoes  
        ✅ Avoid: Tea, coffee immediately after meals  
        ✅ Drink plenty of water  
        """)

    # ✅ Normal Range Comparison Graph
    st.subheader("📊 Hemoglobin Level Comparison")
    normal = 13.0 if gender == "Male" else 12.0

    fig, ax = plt.subplots()
    ax.bar(["Your HB", "Normal HB"], [hb, normal])
    ax.set_ylabel("Hemoglobin (g/dL)")
    ax.set_title("Your HB vs Normal Range")
    st.pyplot(fig)

