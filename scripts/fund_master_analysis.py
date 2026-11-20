
import pandas as pd
import glob

# Load Fund Master dataset
file_path = glob.glob("DATA/RAW/*fund_master.csv")[0]
df = pd.read_csv(file_path)

print("=" * 60)
print("FUND MASTER DATASET ANALYSIS")
print("=" * 60)

# Basic information
print("\n1. DATASET INFORMATION")
print("Shape:", df.shape)
print("Total Schemes:", len(df))

# Unique fund houses
print("\n2. UNIQUE FUND HOUSES")
print("Total Fund Houses:", df["fund_house"].nunique())
print(df["fund_house"].unique())

# Categories
print("\n3. FUND CATEGORIES")
print("Total Categories:", df["category"].nunique())
print(df["category"].value_counts())

# Sub-categories
print("\n4. FUND SUB-CATEGORIES")
print("Total Sub-Categories:", df["sub_category"].nunique())
print(df["sub_category"].value_counts())

# Risk grades
print("\n5. RISK CATEGORIES")
print("Total Risk Categories:", df["risk_category"].nunique())
print(df["risk_category"].value_counts())

# Plan types
print("\n6. PLAN TYPES")
print(df["plan"].value_counts())

# Missing values
print("\n7. MISSING VALUES")
print(df.isnull().sum())

# Fund house and category summary
print("\n8. FUND HOUSE-WISE SCHEME COUNT")
print(df.groupby("fund_house")["scheme_name"].count())

print("\n9. CATEGORY-WISE SCHEME COUNT")
print(df.groupby("category")["scheme_name"].count())

print("\n" + "=" * 60)
print("FUND MASTER ANALYSIS COMPLETED!")
print("=" * 60)
