
import requests
import pandas as pd
import os

# Five mutual fund scheme codes

schemes = {
    "SBI_Large_Cap": 119598,
    "ICICI_Large_Cap": 120586,
    "Nippon_Large_Cap": 118632,
    "Axis_Large_Cap": 120465,
    "Kotak_Large_Cap": 120152
}

output_folder = "DATA/RAW"
os.makedirs(output_folder, exist_ok=True)

for fund_name, scheme_code in schemes.items():

    print("\nFetching:", fund_name)

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        result = response.json()

        scheme_name = result["meta"]["scheme_name"]
        nav_data = result["data"]

        df = pd.DataFrame(nav_data)
        df["scheme_code"] = scheme_code
        df["scheme_name"] = scheme_name

        output_path = os.path.join(
            output_folder,
            f"{fund_name}_{scheme_code}.csv"
        )

        df.to_csv(output_path, index=False)

        print("Scheme Name:", scheme_name)
        print("Scheme Code:", scheme_code)
        print("Total Records:", len(df))
        print("Saved:", output_path)

    except Exception as e:
        print("Error fetching", fund_name, ":", e)

print("\nALL FIVE SCHEME FETCHES COMPLETED!")

