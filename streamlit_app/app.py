import streamlit as st
import numpy as np
import joblib

# Load the trained Random Forest model
model = joblib.load("final_rf_model2.pkl")

st.title("Early Sepsis Prediction")

st.write("Enter patient vitals:")

# Get user input for raw features
HR_mean = st.number_input("Heart Rate (mean)", min_value=0.0, max_value=300.0, value=80.0)
HR_min = st.number_input("Heart Rate (min)", min_value=0.0, max_value=300.0, value=70.0)
HR_std = st.number_input("Heart Rate (std)", min_value=0.0, max_value=50.0, value=5.0)

O2Sat_mean = st.number_input("SpO2 (mean %)", min_value=0.0, max_value=100.0, value=98.0)
O2Sat_min = st.number_input("SpO2 (min %)", min_value=0.0, max_value=100.0, value=95.0)
O2Sat_std = st.number_input("SpO2 (std)", min_value=0.0, max_value=10.0, value=1.0)

Temp_mean = st.number_input("Temperature (mean °C)", min_value=30.0, max_value=45.0, value=37.0)
Temp_min = st.number_input("Temperature (min °C)", min_value=30.0, max_value=45.0, value=36.5)
Temp_max = st.number_input("Temperature (max °C)", min_value=30.0, max_value=45.0, value=37.5)
Temp_std = st.number_input("Temperature (std)", min_value=0.0, max_value=5.0, value=0.5)

SBP_mean = st.number_input("Systolic BP (mean)", min_value=0.0, max_value=300.0, value=120.0)
SBP_max = st.number_input("Systolic BP (max)", min_value=0.0, max_value=300.0, value=130.0)
SBP_std = st.number_input("Systolic BP (std)", min_value=0.0, max_value=50.0, value=5.0)

MAP_max = st.number_input("MAP (max)", min_value=0.0, max_value=200.0, value=90.0)

Resp_mean = st.number_input("Respiration Rate (mean)", min_value=0.0, max_value=100.0, value=18.0)
Resp_min = st.number_input("Respiration Rate (min)", min_value=0.0, max_value=100.0, value=16.0)
Resp_std = st.number_input("Respiration Rate (std)", min_value=0.0, max_value=50.0, value=2.0)

ICULOS = st.number_input("ICU Length of Stay (hours)", min_value=0.0, max_value=1000.0, value=12.0)

# Compute engineered features
HR_range = HR_mean - HR_min
HR_mean_HR_min_ratio = HR_mean / (HR_min + 1e-6)
HR_Resp_interaction = HR_mean * Resp_mean

# Arrange features in the correct order expected by the model
features = np.array([
    HR_std,
    O2Sat_mean, O2Sat_min, O2Sat_std,
    Temp_mean, Temp_min, Temp_max, Temp_std,
    SBP_mean, SBP_max, SBP_std,
    MAP_max,
    Resp_mean, Resp_min, Resp_std,
    ICULOS,
    HR_mean_HR_min_ratio,
    HR_range,
    HR_Resp_interaction
]).reshape(1, -1)

if st.button("Predict"):
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    if prediction == 1:
        st.error(f"Sepsis Likely! (Probability: {probability:.2f})")
    else:
        st.success(f"Sepsis Unlikely (Probability: {probability:.2f})")
