from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

# -----------------------------
# Load trained ML artifacts
# -----------------------------
model = joblib.load("model/fraud_model.pkl")
scaler = joblib.load("model/scaler.pkl")
feature_columns = joblib.load("model/feature_columns.pkl")

# -----------------------------
# Create FastAPI app
# -----------------------------
app = FastAPI(title="Credit Card Fraud Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Input schema (ONLY user inputs)
# -----------------------------
class Transaction(BaseModel):
    amt: float
    category: int
    gender: int
    job: int
    hour: int
    day: int
    month: int
    weekday: int
    lat: float
    long: float
    merch_lat: float
    merch_long: float
    city_pop: float
    distance: float
    unix_time: int

# -----------------------------
# Prediction endpoint
# -----------------------------
@app.post("/predict")
def predict_fraud(data: Transaction):
    input_data = data.dict()

    # 🔒 Build feature row safely
    row = []
    for col in feature_columns:
        # If feature was provided by user, use it
        # Otherwise (training-only feature), use 0
        row.append(input_data.get(col, 0))

    X = np.array([row])

    # Scale input
    X_scaled = scaler.transform(X)

    # Predict
    prediction = int(model.predict(X_scaled)[0])
    probability = float(model.predict_proba(X_scaled)[0][1])

    return {
        "fraud": prediction,
        "probability": round(probability, 4),
        "result": "Fraud Detected" if prediction == 1 else "Legitimate Transaction"
    }

# -----------------------------
# Health check
# -----------------------------
@app.get("/")
def root():
    return {"status": "Fraud Detection API is running"}
