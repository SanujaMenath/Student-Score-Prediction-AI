import streamlit as st
import requests
import json

# --- CONFIGURATION ---
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Student Success AI", page_icon="🎓")

# --- UI HEADER ---
st.title("🎓 AI Student Score Predictor")
st.markdown("Use this tool to predict student performance based on their habits and demographics.")

# --- SIDEBAR INPUTS ---
st.sidebar.header("Student Profile")

# Dropdowns to prevent from typos!
gender = st.sidebar.selectbox("Gender", ["male", "female", "other"])
course = st.sidebar.selectbox("Course", ['b.tech', 'b.sc', 'b.com', 'ba', 'bba', 'bca', 'diploma'])
internet = st.sidebar.selectbox("Internet Access", ["yes", "no"])
sleep_qual = st.sidebar.selectbox("Sleep Quality", ["good", "average", "poor"])
study_method = st.sidebar.selectbox("Study Method", ["self-study", "group study", "coaching", "mixed", "online videos"])
facility = st.sidebar.selectbox("Facility Rating", ["high",  "medium", "low"])
difficulty = st.sidebar.selectbox("Exam Difficulty", ["easy", "moderate",  "hard"])

# Sliders (For numerical values)
age = st.sidebar.slider("Age", 16, 30, 21)
study_hours = st.sidebar.slider("Study Hours (per day)", 0, 15, 5)
attendance = st.sidebar.slider("Class Attendance (%)", 0, 100, 85)
sleep_hours = st.sidebar.slider("Sleep Hours (per night)", 0, 12, 7)

# --- PREDICTION LOGIC ---
if st.button("🚀 Predict Exam Score", type="primary"):
    # 1. Prepare the payload matches Pydantic schema
    payload = {
        "gender": gender,
        "course": course,
        "internet_access": internet,
        "sleep_quality": sleep_qual,
        "study_method": study_method,
        "facility_rating": facility,
        "exam_difficulty": difficulty,
        "age": age,
        "study_hours": study_hours,
        "class_attendance": attendance,
        "sleep_hours": sleep_hours
    }
    
    # 2. Call the API
    with st.spinner("Connecting to AI Brain..."):
        try:
            response = requests.post(API_URL, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                score = result["predicted_exam_score"]
                
                # Display Result nicely
                st.success(f"Predicted Score: **{score:.1f}%**")
                st.progress(int(score))
                
                if score > 75:
                    st.balloons()
            else:
                st.error(f"Error: {response.json().get('detail')}")
                
        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to the API. Is 'uvicorn' running?")