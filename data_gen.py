import pandas as pd
import numpy as np
import os

# Create the data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Set a seed so the "random" numbers are the same every time
np.random.seed(42)

# Generate 1000 rows of data
n_rows = 1000
data = {
'sensor_id': range(1, n_rows + 1),
'temperature': np.random.uniform(40, 110, n_rows),
'vibration': np.random.uniform(2, 20, n_rows),
'pressure': np.random.uniform(100, 500, n_rows),
'humidity': np.random.uniform(30, 90, n_rows),
'device_age': np.random.uniform(0, 10000, n_rows)
}

df = pd.DataFrame(data)

# Logic for Failure (The "Rule" the AI will try to find)
# We say a failure (1) happens if Vibration > 15 AND Age > 8000
df['failure'] = ((df['vibration'] > 15) & (df['device_age'] > 8000)).astype(int)

# Save to the data folder
df.to_csv('sensor_data.csv', index=False)
print("Success! 'sensor_data.csv' has been created in the /data folder.")