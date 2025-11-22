# Rainfall-Prediction-App

## Project Overview
**Rainfall-Prediction-App** is a web application built with **Streamlit** that predicts whether it will rain on a given day based on weather data. It uses a **pre-trained Random Forest model**, so predictions are fast and do not require retraining.  

The app is user-friendly and suitable for anyone interested in weather forecasting, agriculture planning, or data science applications.

---

## Key Features
- Predict rainfall occurrence (Yes / No) based on weather inputs  
- User-friendly web interface with **Streamlit**  
- Pre-trained machine learning model for fast predictions  
- Ready for deployment using **Docker** and **Render**  
- CI/CD workflow included for automatic deployment on GitHub pushes  

---

## Project Structure

Rainfall-Prediction-App/
├── app.py # Streamlit application
├── rainfall_prediction_model.pkl # Pre-trained Random Forest model
├── requirements.txt # Python dependencies
├── Dockerfile # Docker deployment instructions
└── .github/
└── workflows/
└── deploy.yml # CI/CD workflow for GitHub Actions
