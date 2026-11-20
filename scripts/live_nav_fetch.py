
import requests
import pandas as pd
import os

# MFAPI endpoint for HDFC Top 100
url = "https://api.mfapi.in/mf/125497"

# Fetch API response
response = requests.get(url, timeout=30)

# Check API response
response.raise_for_status()

# Convert response into JSON
result = response.json()

# Extract scheme details
scheme_name = result["meta"]["scheme_name"]
scheme_code = result["meta"]["scheme_code"]

print("Scheme Name:", scheme_name)
print("Scheme Code:", scheme_code)

# Extract NAV records
nav_data = result["data"]

# Convert JSON records into DataFrame
df = pd.DataFrame(nav_data)

# Add scheme information
df["scheme_code"] = scheme_code
df["scheme_name"] = scheme_name

# Save as raw CSV
output_folder = "DATA/RAW"
os.makedirs(output_folder, exist_ok=True)

output_path = os.path.join(
    output_folder,
    "live_nav_125497.csv"
)

df.to_csv(output_path, index=False)

# Display results
print("\nNAV DATA FETCHED SUCCESSFULLY!")
print("Total Records:", len(df))
print("\nFirst Five Records:")
print(df.head())

print("\nSaved Location:", output_path)
