import joblib
import pandas as pd

# Load the brain you just trained
model = joblib.load('predictive_model.pkl')

# Simulate a "Failing Machine" (High vibration and old age)
# Format: [temperature, vibration, pressure, humidity, device_age]
new_data = pd.DataFrame([[85.5, 18.2, 400.0, 65.0, 9000]],
columns=['temperature', 'vibration', 'pressure', 'humidity', 'device_age'])

prediction = model.predict(new_data)

if prediction[0] == 1:
    print("🚨 ALERT: Machine Failure Predicted! Schedule Maintenance.")
else:
    print("✅ Status: Machine Healthy.")