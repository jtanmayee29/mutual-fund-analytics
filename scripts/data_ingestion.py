
import pandas as pd
import os

# Folder containing raw CSV datasets
DATA_FOLDER = "DATA/RAW"

# Get all CSV files
csv_files = [file for file in os.listdir(DATA_FOLDER)
             if file.lower().endswith(".csv")]

print("TOTAL CSV FILES FOUND:", len(csv_files))
print("=" * 60)

# Load and inspect each dataset
for file in csv_files:

    file_path = os.path.join(DATA_FOLDER, file)

    print("\nDATASET:", file)
    print("-" * 60)

    try:
        df = pd.read_csv(file_path)

        # Display dataset shape
        print("Shape:", df.shape)

        # Display column names and data types
        print("\nColumn Names and Data Types:")
        print(df.dtypes)

        # Display first five rows
        print("\nFirst Five Rows:")
        print(df.head())

    except Exception as e:
        print("Error loading dataset:", e)

print("\nDATA INGESTION COMPLETED!")
