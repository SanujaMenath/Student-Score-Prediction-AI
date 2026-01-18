# 🎓 EduMetrics AI: Student Performance Prediction System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://https://share.streamlit.io])
[![API Status](https://img.shields.io/badge/API-Online-green)](https://render.com)
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
* **Web Dashboard:** [Click here to launch the App](https://student-score-prediction-ai-ylefamztjrjcpndjsqyn3b.streamlit.app)
* **API Documentation:** [Click here to view Swagger UI](https://student-score-prediction-ai.onrender.com)

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
---

## Model & Data overview

Key feature groups:
- Categorical (encoded with LabelEncoder): `gender`, `course`, `internet_access`, `sleep_quality`, `study_method`, `facility_rating`, `exam_difficulty`
- Numerical (scaled with StandardScaler): `age`, `study_hours`, `class_attendance`, `sleep_hours`

Target:
- `exam_score` (continuous regression target, likely a percent)

Model architecture (from `test_scores.py`):
- Embedding inputs for each categorical column
- Concatenate embeddings + numerical inputs
- Dense layers: 256 -> 128 -> 64 -> 1 (linear output)
- Loss: MSE, metric: RMSE
- Callbacks: EarlyStopping with restore best weights

Artifacts expected by the API:
- `student_score_model.keras` (Keras saved model)
- `label_encoders.pkl` (joblib dict of LabelEncoder instances)
- `scaler.pkl` (joblib StandardScaler)

---
## Setup & Installation

Recommended: clone the repository and use the provided devcontainer or a Python virtual environment.

1. Clone the repo
```bash
git clone https://github.com/SanujaMenath/Student-Score-Prediction-AI.git
cd Student-Score-Prediction-AI
```

### Recommended (local / devcontainer)
- Open in VS Code and use the `.devcontainer/devcontainer.json` to spin up a reproducible environment.
- The devcontainer runs `streamlit run dashboard.py` on attach (see file for details).

### Python virtualenv
```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
# If no requirements.txt exists yet, install the minimal set below
```

### Install Dependencies
```bash
pip install -r requirements.txt
```  
If there's no `requirements.txt`, install:
```bash
pip install fastapi uvicorn pandas scikit-learn joblib tensorflow streamlit requests
```
Note: TensorFlow version should be compatible with your OS/GPU. Installing TF in devcontainers or containers is recommended for reproducible results.

---
