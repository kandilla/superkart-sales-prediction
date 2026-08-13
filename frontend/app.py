import streamlit as st
import requests
import numpy as np

st.title("SuperKart Sales Prediction")

backend_url = st.text_input("Backend URL", "https://your-forwarded-url/predict")

features = st.text_input("Enter comma-separated features")

if st.button("Predict"):
    features_list = [float(x) for x in features.split(",")]
    payload = {"features": features_list}
    response = requests.post(backend_url, json=payload)
    st.write(response.json())
