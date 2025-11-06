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
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import datetime
import os

# Load Model
model = joblib.load("model.pkl")

st.title("🩸 AnemiaSense - Anemia Detection Using ML")
st.write("Enter the values below to check your anemia status.")

# Sidebar Info
st.sidebar.header("📊 Model Information")
st.sidebar.write("✅ Model Used: Random Forest Classifier")
st.sidebar.write("📌 Dataset Used: anemia.csv")

# Optional Dataset Display
if st.checkbox("Show sample dataset"):
    df = pd.read_csv("anemia.csv")
    st.write(df.head())

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
hb = st.number_input("Hemoglobin (g/dL)", min_value=1.0, max_value=20.0, value=13.5)
mch = st.number_input("MCH", min_value=1.0, max_value=40.0, value=25.0)
mchc = st.number_input("MCHC", min_value=15.0, max_value=40.0, value=30.0)
mcv = st.number_input("MCV", min_value=50.0, max_value=120.0, value=80.0)

# Prediction Button
if st.button("Check Anemia Status"):
    
    gender_num = 0 if gender == "Male" else 1
    input_data = np.array([[gender_num, hb, mch, mchc, mcv]])
    prediction = model.predict(input_data)[0]

    # ✅ Risk Level
    if (gender == "Male" and hb < 13) or (gender == "Female" and hb < 12):
        risk_level = "High"
    elif (gender == "Male" and 13 <= hb < 13.5) or (gender == "Female" and 12 <= hb < 12.5):
        risk_level = "Moderate"
    else:
        risk_level = "Normal"

    # ✅ Result Display
    if prediction == 1:
        st.error(f"🔴 Result: The person is ANEMIC.\n⚠ Risk Level: **{risk_level}**")
    else:
        st.success(f"🟢 Result: The person is NOT anemic.\n✅ Risk Level: **Normal**")

    # ✅ Diet Tips
    if prediction == 1:
        st.subheader("🍎 Suggested Diet for Anemia")
        st.write("""
        ✅ Iron-rich foods: Spinach, beetroot, meat, liver, beans  
        ✅ Vitamin C: Lemon, orange, kiwi  
        ✅ Vitamin B12 foods: Eggs, dairy, chicken  
        ✅ Avoid tea/coffee immediately after meals (reduces iron absorption)  
        """)

    # ✅ Graph Comparison
    st.subheader("📊 Blood Value Comparison")

    normal_vals = [13 if gender == "Male" else 12, 27, 33, 90]
    user_vals = [hb, mch, mchc, mcv]
    labels = ["Hemoglobin", "MCH", "MCHC", "MCV"]

    fig2, ax2 = plt.subplots()
    ax2.bar(labels, user_vals, label="Your Values")
    ax2.plot(labels, normal_vals, marker='o', label="Normal Level")
    ax2.legend()
    st.pyplot(fig2)

    # ✅ Save History
    result_text = "Anemic" if prediction == 1 else "Not Anemic"
    log = pd.DataFrame([[datetime.datetime.now(), gender, hb, mch, mchc, mcv, result_text, risk_level]],
                       columns=["Date", "Gender", "HB", "MCH", "MCHC", "MCV", "Result", "Risk Level"])

    if os.path.exists("history.csv"):
        log.to_csv("history.csv", mode='a', header=False, index=False)
    else:
        log.to_csv("history.csv", index=False)

    st.success("✅ Result saved to history!")

# ✅ Show Previous Records
if st.button("Show Previous Records"):
    if os.path.exists("history.csv"):
        history = pd.read_csv("history.csv")
        st.write(history)
    else:
        st.info("No history found yet.")

# ✅ Model Performance
if st.button("Show Model Performance"):
    df = pd.read_csv("anemia.csv")

    # automatically detect target column
    target_col = None
    for col in df.columns:
        if col.lower() in ["anemia", "result", "class", "label", "target"]:
            target_col = col
            break

    if target_col is None:
        st.error("❌ Error: No target column named 'anemia' or 'result' found in dataset.")
    else:
        X = df.drop(target_col, axis=1)
        y = df[target_col]
        y_pred = model.predict(X)

        accuracy = accuracy_score(y, y_pred)
        st.info(f"📊 Model Accuracy: **{accuracy*100:.2f}%**")

        st.subheader("✅ Confusion Matrix")
        cm = confusion_matrix(y, y_pred)
        st.write(pd.DataFrame(cm, columns=["Predicted 0", "Predicted 1"], index=["Actual 0", "Actual 1"]))

        st.subheader("✅ Classification Report")
        st.text(classification_report(y, y_pred))
