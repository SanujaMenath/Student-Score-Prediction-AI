# 🎓 EduMetrics AI: Student Performance Prediction System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://edumetrics-ai.streamlit.app](https://student-score-prediction-ai-ylefamztjrjcpndjsqyn3b.streamlit.app))
[![API Status](https://img.shields.io/badge/API-Online-green)](https://student-score-prediction-ai.onrender.com)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **A production-grade Deep Learning application that predicts student exam performance based on demographic and behavioral data.**

---

## 📖 Project Overview
**EduMetrics AI** is a full-stack machine learning application designed to help educational institutions identify at-risk students early. Unlike traditional rule-based systems, this project utilizes a **Multi-Input Deep Neural Network** (built with TensorFlow/Keras) to analyze complex, non-linear interactions between study habits, sleep quality, and academic performance.

The system is deployed using a modern **Client-Server Architecture**:
* **The Brain (Backend):** A high-performance FastAPI server hosting the trained model.
* **The Face (Frontend):** An interactive Streamlit dashboard for real-time user predictions.

---

## 🚀 Live Demo
* **Web Dashboard:** [Click here to launch the App](https://[YOUR-STREAMLIT-APP-URL].streamlit.app)
* **API Documentation:** [Click here to view Swagger UI](https://[YOUR-RENDER-URL].onrender.com/docs)

*(Note: The API is hosted on a free instance and may take 50 seconds to "wake up" on the first request.)*

---

## 🛠️ Tech Stack
* **Deep Learning:** TensorFlow, Keras (Functional API)
* **Backend API:** FastAPI, Uvicorn, Pydantic
* **Frontend:** Streamlit
* **Data Processing:** Pandas, Scikit-Learn (LabelEncoding, StandardScaler)
* **Deployment:** Render (Backend), Streamlit Cloud (Frontend)

---

## 📂 Project Structure
```bash
student-score-prediction-ai/
├── 📂 .streamlit/          # Streamlit configuration
├── 📄 main.py              # FastAPI Backend (The "Brain")
├── 📄 dashboard.py         # Streamlit Frontend (The "Face")
├── 📄 train.ipynb          # Jupyter Notebook for Model Training & EDA
├── 📄 requirements.txt     # Python dependencies
├── 📄 student_score_model.keras  # The trained Deep Learning Model
├── 📄 label_encoders.pkl   # Saved encoders for categorical data
└── 📄 scaler.pkl           # Saved scaler for numerical data
```
