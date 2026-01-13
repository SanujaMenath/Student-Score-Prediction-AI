import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import tensorflow as tf
import joblib

# --- 1. SETUP LOGGING (Production Requirement) ---
# This tracks every event, error, and prediction in your terminal
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Student Score Prediction API",
    description="Production-ready API for predicting student exam scores.",
    version="1.0.0"
)

# --- 2. CORS POLICY (Security Requirement) ---
# Allows your frontend (running on a different port) to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In real production, replace "*" with specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 3. INPUT VALIDATION SCHEMA ---
class StudentInput(BaseModel):
    gender: str
    course: str
    internet_access: str
    sleep_quality: str
    study_method: str
    facility_rating: str
    exam_difficulty: str
    age: float
    study_hours: float
    class_attendance: float
    sleep_hours: float

# --- 4. LOAD ARTIFACTS ON STARTUP ---
try:
    model = tf.keras.models.load_model("student_score_model.keras")
    encoders = joblib.load("label_encoders.pkl")
    scaler = joblib.load("scaler.pkl")
    logger.info("✅ All model artifacts loaded successfully.")
except Exception as e:
    logger.error(f"❌ Failed to load artifacts: {e}")
    raise RuntimeError("Model files missing. Check server logs.")

# Define column groups
categorical_cols = [
    "gender", "course", "internet_access",
    "sleep_quality", "study_method", 
    "facility_rating", "exam_difficulty"
]
numerical_cols = [
    "age", "study_hours", 
    "class_attendance", "sleep_hours"
]

@app.get("/")
def health_check():
    """Simple health check endpoint for monitoring tools."""
    return {"status": "running", "model_loaded": True}

@app.post("/predict")
def predict_score(data: StudentInput):
    """
    Receives student data and returns a predicted exam score.
    """
    try:
        # Convert input to DataFrame
        input_data = data.dict()
        df = pd.DataFrame([input_data])
        
        logger.info(f"📥 Received prediction request for Age: {data.age}, Course: {data.course}")

        # Preprocessing Loop
        for col, le in encoders.items():
            if col in df.columns:
                # Automate lowercasing to handle "Male" vs "male" issues
                raw_val = str(df[col].iloc[0]).lower().strip()
                
                # Check validity
                if raw_val not in le.classes_:
                    valid_opts = list(le.classes_)
                    logger.warning(f"⚠️ Invalid category '{raw_val}' in {col}")
                    raise HTTPException(status_code=400, detail=f"Invalid {col}: '{raw_val}'. Valid options: {valid_opts}")
                
                # Transform
                df[col] = le.transform([raw_val])

        # Scale numericals
        df[numerical_cols] = scaler.transform(df[numerical_cols])

        # Prepare 8 Inputs for the Functional Model
        model_inputs = [df[col] for col in categorical_cols] + [df[numerical_cols]]

        # Predict
        prediction = model.predict(model_inputs)
        result = float(prediction[0][0])
        
        logger.info(f"✅ Prediction success: {result:.2f}")
        return {"predicted_exam_score": result}

    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"❌ Prediction Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))