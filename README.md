# AI-IoT Predictive Maintenance Prototype

## 📌 Project Overview
This project demonstrates an end-to-end AI pipeline for industrial IoT. It simulates real-time sensor data and uses a **Random Forest** machine learning model to predict equipment failure before it happens.

## 🛠️ Technical Workflow
1. **Data Generation (`data_gen.py`):** Creates a synthetic dataset simulating Vibration, Temperature, and Device Age.
2. **Model Training (`train_model.py`):** Trains the AI to recognize patterns that lead to "Failure" (1) vs "Normal" (0).
3. **Inference (`predict.py`):** Uses the trained model to provide maintenance alerts.

## 🚀 How to Run
1. **Install Dependencies:**
```bash
pip install pandas scikit-learn joblib
