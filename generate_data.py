import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Lock the random seed so our mathematical results are perfectly reproducible
np.random.seed(42)

# 1. Generate Baseline Data (90 days of hourly data)
print("Initializing baseline data distribution...")
hours = 90 * 24
dates = [datetime(2026, 1, 1) + timedelta(hours=i) for i in range(hours)]

# Normal distribution for price (Mean=$100, Standard Deviation=$2)
prices = np.random.normal(loc=100, scale=2, size=hours)

# Normal distribution for inventory (Mean=500 units, Standard Deviation=20 units)
inventory = np.random.normal(loc=500, scale=20, size=hours).astype(int)

df = pd.DataFrame({'timestamp': dates, 'price': prices, 'inventory': inventory})

# 2. Inject the "Poison" (Our target anomalies)
print("Injecting mathematical anomalies...")

# Poison 1: The Flash Crash (Sudden, massive drop in price)
df.loc[500, 'price'] = 12.50 

# Poison 2: The Impossible Glitch (Negative inventory, which physically cannot exist)
df.loc[1200, 'inventory'] = -45 

# Poison 3: The Silent Creep (A slow, statistical deviation over 7 days)
creep_start = 1800
creep_duration = 24 * 7
for i in range(creep_duration):
    df.loc[creep_start + i, 'price'] += (i * 0.15) 

# 3. Export the Environment
# Format price to 2 decimal places for real-world currency accuracy
df['price'] = df['price'].round(2)

file_name = 'synthetic_market_data.csv'
df.to_csv(file_name, index=False)
print(f"SUCCESS: Target environment '{file_name}' generated with {hours} records.")