🌧️ Rainfall Prediction App

A machine learning web application that predicts whether it will rain or not based on daily weather conditions. Built using Streamlit, powered by a pre-trained Random Forest model, and fully deployable with Docker and CI/CD (GitHub Actions + Render).

📌 Project Overview

The Rainfall Prediction App takes weather parameters such as pressure, humidity, cloud cover, wind speed, and more to predict the likelihood of rainfall.
The model is pre-trained, ensuring instant predictions without requiring on-the-fly training.

This project is ideal for:

- Weather forecasting demos

- Agriculture-related decision support

- ML deployment & MLOps practice

- Streamlit-based application development

⭐ Key Features

🔮 Predicts Rainfall / No Rainfall using a machine learning model

🧠 Uses a pre-trained Random Forest classifier

🖥️ Interactive Streamlit UI

🐳 Fully containerized via Docker

🚀 Deployable on Render

🔁 Includes CI/CD pipeline using GitHub Actions

📁 Project Structure
Rainfall-Prediction-App/
├── app.py                     # Streamlit application
├── rainfall_prediction_model.pkl   # Pre-trained ML model
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker deployment instructions
└── .github/
    └── workflows/
        └── deploy.yml         # CI/CD pipeline for automatic deployments

🚀 Live Demo

👉 Hosted on Render:
https://rainfall-prediction-app-159o.onrender.com/

🛠️ Technologies Used

- Python

- Streamlit

- Scikit-learn

- Pandas & NumPy

- Docker

- GitHub Actions (CI/CD)

- Render Cloud Deployment

🧪 How to Run Locally
# Clone the repository
- git clone https://github.com/vinayak533/Rainfall-Prediction-App.git
- cd Rainfall-Prediction-App

# Install dependencies
- pip install -r requirements.txt

# Run the Streamlit app
- streamlit run app.py

🐳 Run with Docker
- docker build -t rainfall-app .
- docker run -p 8501:8501 rainfall-app

🔁 CI/CD (GitHub Actions)

The project includes a GitHub Actions workflow that:

- Installs dependencies

- Runs tests (placeholder)

- Triggers auto-deployment on Render (if connected)

- Every push to the main branch automatically updates the deployed app.

📬 About

A complete, production-ready Machine Learning application demonstrating:

- ML model deployment

- MLOps fundamentals

- Cloud hosting

- Docker containerization

- Automated CI/CD pipelines

This project is part of my ongoing journey into Machine Learning, Data Science, and MLOps.
