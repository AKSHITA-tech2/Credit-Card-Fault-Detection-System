# 💳 Credit Card Fraud Detection System

**End-to-End Machine Learning Application with FastAPI & Web Frontend**

---

## 📌 Overview

The **Credit Card Fraud Detection System** is a production-style machine learning project that detects fraudulent transactions in real time.

It demonstrates the **complete ML lifecycle**:

> **Data preprocessing → model training → API deployment → frontend inference**

Unlike notebook-only projects, this system focuses on **real-world ML engineering practices**, including:

* feature consistency between training & inference
* API-based prediction serving
* scalable backend design
* clean Git workflows
* deployment-ready architecture

---

## 🚀 Key Features

* ✅ Real-time fraud prediction using a trained ML model
* ✅ REST API built with **FastAPI**
* ✅ Interactive web frontend for transaction input
* ✅ Robust preprocessing & scaling aligned with training pipeline
* ✅ Strict feature-ordering enforcement at inference time
* ✅ Industry-grade handling of unseen inputs
* ✅ Clean Git repository (no datasets or large artifacts committed)

---

## 🧠 Machine Learning Details

* **Problem Type:** Binary Classification (Fraud vs Legitimate)
* **Model:** Logistic Regression
* **Preprocessing:**

  * Standardization using `StandardScaler`
  * Deterministic feature ordering for inference
* **Evaluation:** Probability-based fraud scoring

> ⚠️ *Special care was taken to prevent training-inference mismatch — one of the most common real-world ML deployment failures.*

---

## 🏗 Project Architecture

```
Credit-Card-Fraud-Detection-System/
│
├── api.py                 # FastAPI backend
├── frontend/
│   └── index.html         # Web UI
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/                  # (ignored) datasets
├── model/                 # (ignored) trained artifacts
├── notebooks/             # (ignored) experiments
└── .venv/                 # (ignored) virtual env
```

---

## 🛠 Tech Stack

### Languages & Libraries

* Python
* NumPy
* scikit-learn
* FastAPI
* Pydantic
* HTML / CSS / JavaScript

### Tools

* Git & GitHub
* VS Code
* PowerShell
* Python `venv`

---

## 🔌 API Endpoints

### ✅ Health Check

```
GET /
```

Response:

```json
{
  "status": "Fraud Detection API is running"
}
```

---

### 🔮 Fraud Prediction

```
POST /predict
```

#### Sample Request

```json
{
  "amt": 150.75,
  "category": 2,
  "gender": 1,
  "job": 45,
  "hour": 14,
  "day": 12,
  "month": 6,
  "weekday": 2,
  "lat": 37.7749,
  "long": -122.4194,
  "merch_lat": 37.775,
  "merch_long": -122.418,
  "city_pop": 870000,
  "distance": 2.35,
  "unix_time": 1710000000
}
```

#### Sample Response

```json
{
  "fraud": 0,
  "probability": 0.0824,
  "result": "Legitimate Transaction"
}
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/AKSHITA-tech2/Credit-Card-Fault-Detection-System.git
cd Credit-Card-Fault-Detection-System
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Start API Server

```bash
python -m uvicorn api:app --reload
```

Visit:

👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 5️⃣ Launch Frontend

* Open `frontend/index.html` using VS Code **Live Server**
* Enter transaction details
* Receive fraud predictions instantly

---

## 📂 Dataset Notes

To keep the repository lightweight:

* datasets are excluded
* trained models are excluded
* artifacts can be regenerated locally

Place raw datasets inside:

```
data/
```

Retrain models to recreate artifacts.

---

## 🎯 Key Learning Outcomes

This project showcases:

* end-to-end ML system engineering
* feature-safe deployment pipelines
* REST-based ML serving
* inference-time validation
* debugging production ML issues
* Git hygiene for ML workflows
* scalable API design

> 💬 *In real ML systems, deployment mistakes often matter more than raw model accuracy — this project was designed to prevent exactly those failures.*

---

## 🔮 Future Improvements

* 📊 Fraud probability visualization
* 🗄 Store predictions in MySQL
* 🔐 Authentication system
* ☁ Cloud deployment (Render / Railway)
* 🐳 Docker containerization

---

## 👤 Author

**Akshita Raghavan**

* GitHub: [https://github.com/AKSHITA-tech2](https://github.com/AKSHITA-tech2)

---

