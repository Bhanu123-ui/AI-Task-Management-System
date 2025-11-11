import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load saved models and preprocessing files
model = joblib.load("data/final_priority_model.pkl")
vectorizer = joblib.load("data/final_tfidf_vectorizer.pkl")
scaler = joblib.load("data/final_numeric_scaler.pkl")
le = joblib.load("data/label_encoder.pkl")

# Streamlit UI
st.set_page_config(page_title="AI Task Management", layout="centered")
st.title("🧠 AI-Powered Task Management System")

st.markdown("### Predict task priority using your trained ML model!")

# Input fields
task_description = st.text_area("Task Description", "Complete backend testing and deployment")
days_left = st.number_input("Days Left until Deadline", min_value=0, max_value=60, value=3)
workload_hours = st.number_input("Estimated Workload (hours)", min_value=0.0, max_value=24.0, value=5.0)

# Prediction function
def predict_priority(task_description, days_left, workload_hours):
    X_text = vectorizer.transform([task_description]).toarray()
    X_num = pd.DataFrame([[days_left, workload_hours]], columns=["days_left", "workload_hours"])
    X_num_scaled = scaler.transform(X_num)
    X_input = np.hstack((X_text, X_num_scaled))
    pred_encoded = model.predict(X_input)[0]
    pred_label = le.inverse_transform([pred_encoded])[0]
    return pred_label

if st.button("Predict Priority"):
    prediction = predict_priority(task_description, days_left, workload_hours)
    st.success(f"🎯 Predicted Priority: **{prediction}**")
