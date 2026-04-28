import pandas as pd
import numpy as np

print("Initiating OVERSEER_V2 Diagnostic Engine...")

# 1. Ingest the Data
df = pd.read_csv('synthetic_market_data.csv')

# 2. Mathematical Audit: Z-Score Calculation
mean_price = df['price'].mean()
std_price = df['price'].std()

# Calculate the precise mathematical deviation for every single row
df['price_z_score'] = (df['price'] - mean_price) / std_price

# 3. Threat Isolation
print("Scanning for statistical and logical deviations...")

# Threat 1: Price Anomalies (Isolating the Flash Crash and the Creep)
price_anomalies = df[(df['price_z_score'] > 3) | (df['price_z_score'] < -3)].copy()
price_anomalies['threat_type'] = 'STATISTICAL_PRICE_DEVIATION'

# Threat 2: Logic Failures (Isolating the Impossible Glitch)
inventory_anomalies = df[df['inventory'] < 0].copy()
inventory_anomalies['threat_type'] = 'LOGIC_FAILURE_NEGATIVE_STOCK'

# 4. Compile the Threat Matrix
threat_matrix = pd.concat([price_anomalies, inventory_anomalies])

# Strip away the working math columns to provide a clean deliverable to the "client"
threat_output = threat_matrix[['timestamp', 'price', 'inventory', 'threat_type']]

# 5. Export the Deliverable
report_name = 'THREAT_REPORT.csv'
threat_output.to_csv(report_name, index=False)
print(f"AUDIT COMPLETE: {len(threat_output)} anomalies successfully isolated to '{report_name}'.")