# 🚔 Crime Pattern Detection System

## 📌 Overview

A data-driven system that analyzes historical crime data to detect patterns, generate risk scores, and predict future crime trends.

---

## 🚀 Features

### ✅ Core Features

* Data ingestion and preprocessing
* Exploratory data analysis
* Crime pattern detection using clustering
* Visualization-ready structured data

---

### 🔥 Unique Feature

**Smart Crime Risk Scoring System**

* Generates a normalized risk score (0–1)
* Categorizes regions into LOW / MEDIUM / HIGH risk
* Enables decision-making insights

---

### 🤖 Advanced Feature

**Crime Prediction Model**

* Uses Random Forest Regressor
* Predicts total IPC crimes
* Evaluated using MAE metric

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib / Seaborn

---

## ⚙️ Setup Instructions

```bash
git clone <your-repo>
cd crime-pattern-detection

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python main.py
```

---

## 📊 Sample Output

```
STATE/UT   YEAR   Risk_Score   Risk_Level
Delhi      2010   0.82         HIGH
Goa        2010   0.21         LOW
```

---

## 📈 Future Improvements

* Time-series forecasting (ARIMA / LSTM)
* Real-time crime data integration
* Interactive dashboard (Streamlit / React)
* Geo-based heatmaps

---

## 🧠 Learnings

* Data preprocessing pipeline design
* Clustering for pattern detection
* Feature engineering for risk scoring
* ML model building and evaluation

---
