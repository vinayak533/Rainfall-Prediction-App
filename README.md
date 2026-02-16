# 🌧️ Rainfall Prediction App

## 📌 Summary

This project is a machine learning web application that predicts whether it will rain based on weather conditions using a pre-trained Random Forest model. The application is built with Streamlit and includes Docker deployment and CI/CD automation for production-ready ML serving.

---

## 🛠️ Technologies Used

* Python
* Scikit-learn (Random Forest)
* Streamlit
* Pandas & NumPy
* Docker
* GitHub Actions (CI/CD)
* Render Cloud Deployment

---

## ✨ Features

* Predicts Rainfall / No Rainfall instantly
* Pre-trained Random Forest model for fast inference
* Interactive Streamlit user interface
* Docker containerization for deployment
* Automated CI/CD pipeline
* Cloud deployment support (Render)
* User-friendly weather parameter input

---

## ⌨️ Keyboard Shortcuts

```
Ctrl + C   → Stop application
Enter      → Submit command
Up Arrow   → Reuse previous command
```

---

## ⚙️ Process

```
1. User enters weather parameters in the Streamlit UI
2. Input data is processed and formatted
3. Pre-trained model predicts rainfall outcome
4. Prediction result is displayed to the user
```

---

## 🏗️ How I Built It

```
- Trained a Random Forest model using weather data
- Saved the trained model using pickle
- Built interactive UI using Streamlit
- Containerized the application using Docker
- Implemented CI/CD pipeline with GitHub Actions
- Deployed application to Render cloud platform
```

---

## 📚 What I Learned

```
- Machine learning model deployment
- Streamlit application development
- Docker containerization
- CI/CD automation with GitHub Actions
- Cloud deployment workflows
- End-to-end ML project lifecycle
```

---

## 🚀 How It Could Be Improved

```
- Add real-time weather API integration
- Improve UI with data visualization dashboards
- Implement model monitoring and logging
- Add historical rainfall analysis
- Deploy using Kubernetes for scalability
- Use advanced models for improved accuracy
```

---

## ▶️ How to Run the Project

### Clone Repository

```bash
git clone https://github.com/yourusername/Rainfall-Prediction-App.git
cd Rainfall-Prediction-App
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

## 🐳 Run with Docker

```bash
docker build -t rainfall-app .
docker run -p 8501:8501 rainfall-app
```

Open in browser:

```
http://localhost:8501
```

---

## 📂 Project Structure

```
Rainfall-Prediction-App/
│
├── app.py
├── rainfall_prediction_model.pkl
├── requirements.txt
├── Dockerfile
│
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## ⭐ About

A production-ready machine learning application that predicts rainfall using a pre-trained Random Forest model with Streamlit, Docker, CI/CD, and cloud deployment support.
