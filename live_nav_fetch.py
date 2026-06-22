import requests
import pandas as pd

funds = {
    "sbi_bluechip": "119551",
    "icici_bluechip": "120503",
    "nippon_large_cap": "118632",
    "axis_bluechip": "119092",
    "kotak_bluechip": "120841"
}

for fund_name, scheme_code in funds.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_data = data.get("data", [])

        df = pd.DataFrame(nav_data)

        filename = f"data/raw/{fund_name}_nav.csv"

        df.to_csv(filename, index=False)

        print(f"{fund_name} saved successfully!")

    else:
        print(f"Failed to fetch {fund_name}")