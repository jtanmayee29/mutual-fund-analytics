
import pandas as pd
import glob
import os

# Load datasets
fund_file = glob.glob("DATA/RAW/*fund_master.csv")[0]
nav_file = glob.glob("DATA/RAW/*nav_history.csv")[0]

fund_master = pd.read_csv(fund_file)
nav_history = pd.read_csv(nav_file)

# Make sure scheme codes have the same data type
fund_master["amfi_code"] = pd.to_numeric(
    fund_master["amfi_code"], errors="coerce"
)

nav_history["amfi_code"] = pd.to_numeric(
    nav_history["amfi_code"], errors="coerce"
)

# Get unique scheme codes
fund_codes = fund_master[["amfi_code", "scheme_name"]].drop_duplicates(
    subset="amfi_code"
)

nav_codes = nav_history[["amfi_code"]].drop_duplicates()

# Compare both datasets
validation = fund_codes.merge(
    nav_codes,
    on="amfi_code",
    how="left",
    indicator=True
)

# Separate matching and missing codes
matched = validation[validation["_merge"] == "both"]
missing = validation[validation["_merge"] == "left_only"]

# Display results
print("=" * 55)
print("AMFI SCHEME CODE VALIDATION REPORT")
print("=" * 55)

print("\nTotal unique codes in Fund Master:", len(fund_codes))
print("Total unique codes in NAV History:", len(nav_codes))
print("Matching scheme codes:", len(matched))
print("Missing scheme codes:", len(missing))

print("\nMATCHING SCHEMES:")
print(matched[["amfi_code", "scheme_name"]].to_string(index=False))

print("\nMISSING SCHEMES:")
if missing.empty:
    print("No missing scheme codes!")
else:
    print(missing[["amfi_code", "scheme_name"]].to_string(index=False))

# Save missing codes report
os.makedirs("REPORTS", exist_ok=True)

missing.to_csv(
    "REPORTS/missing_amfi_codes.csv",
    index=False
)

# Save summary report
with open("REPORTS/amfi_validation_report.txt", "w") as file:
    file.write("AMFI SCHEME CODE VALIDATION REPORT\n")
    file.write("=" * 40 + "\n")
    file.write(f"Fund Master unique codes: {len(fund_codes)}\n")
    file.write(f"NAV History unique codes: {len(nav_codes)}\n")
    file.write(f"Matching codes: {len(matched)}\n")
    file.write(f"Missing codes: {len(missing)}\n")

print("\nReports saved inside REPORTS folder.")
print("\nAMFI VALIDATION COMPLETED!")
