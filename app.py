import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("rainfall_prediction_model.pkl", "rb") as file:
    model_data = pickle.load(file)

model = model_data["model"]
feature_names = model_data["feature_names"]

st.title("Rainfall Prediction App")
st.write("Predict whether it will rain based on weather data.")

# User inputs
pressure = st.number_input("Pressure (hPa)", value=1015.0)
dewpoint = st.number_input("Dewpoint (°C)", value=19.0)
humidity = st.number_input("Humidity (%)", value=80)
cloud = st.number_input("Cloud Cover (%)", value=40)
sunshine = st.number_input("Sunshine Hours", value=0.0)
winddirection = st.number_input("Wind Direction (°)", value=45)
windspeed = st.number_input("Wind Speed (km/h)", value=15)

# Prepare input for prediction
input_data = pd.DataFrame([[pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]],
                          columns=feature_names)

if st.button("Predict"):
    prediction = model.predict(input_data)
    result = "Rainfall" if prediction[0] == 1 else "No Rainfall"
    st.success(f"Prediction: {result}")
