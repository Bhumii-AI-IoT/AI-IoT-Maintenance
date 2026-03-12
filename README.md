# AI-IoT Predictive Maintenance Prototype
**Field:** Industrial Automation / Predictive Analytics

### Project Overview
This repository contains a functional AI pipeline designed to monitor industrial equipment and predict mechanical failure before it occurs.

### Technical Architecture
- **Sensing:** `data_gen.py` creates a digital twin of sensor data (Vibration, Temp).
- **Learning:** `train_model.py` uses a Random Forest algorithm to identify failure patterns.
- **Inference:** `predict.py` provides real-time alerts for maintenance teams.

### Patent Significance
The model specifically targets the correlation between **high vibration (>15mm/s)** and **high device age**, a key indicator of mechanical fatigue in heavy machinery.
