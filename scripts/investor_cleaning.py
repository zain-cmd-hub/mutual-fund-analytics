import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Validate amount
invalid_amount = (df["amount_inr"] <= 0).sum()

# Check KYC values
print("Unique KYC Status:")
print(df["kyc_status"].unique())

print("\nInvalid Amount Records:", invalid_amount)

# Save cleaned file
df.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("\nInvestor transactions cleaned successfully!")