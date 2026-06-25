import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by AMFI code and date
df = df.sort_values(by=["amfi_code", "date"])

# Forward fill missing NAV within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove duplicate rows
before = len(df)
df = df.drop_duplicates()
after = len(df)

# Validate NAV values
invalid_nav = (df["nav"] <= 0).sum()

print("Rows before removing duplicates :", before)
print("Rows after removing duplicates  :", after)
print("Invalid NAV values (<=0)        :", invalid_nav)

# Save cleaned file
df.to_csv("data/processed/02_nav_history_cleaned.csv", index=False)

print("\nCleaned file saved successfully!")