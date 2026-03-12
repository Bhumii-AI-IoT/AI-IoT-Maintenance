import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import os
data_path = 'data/sensor_data.csv'
# Check if data exists
if not os.path.exists(data_path):
    print("Error: Run data_gen.py first!")
    exit() # This stops the script if the file is missing

# Load data (These must NOT be indented)
data = pd.read_csv(data_path)
X = data[['temperature', 'vibration', 'pressure', 'humidity', 'device_age']]
y = data['failure']
# 1. Split the data into Training and Testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Initialize the AI Model
print("AI is learning patterns...")
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 3. Train the model
model.fit(X_train, y_train)

# 4. Save the model for later use
joblib.dump(model, 'predictive_model.pkl')
print("Success! Model trained and saved as 'predictive_model.pkl'")

from sklearn.metrics import classification_report

# Make predictions on the test set
y_pred = model.predict(X_test)

# Print the report
print("\n--- Model Performance Report ---")
print(classification_report(y_test, y_pred))