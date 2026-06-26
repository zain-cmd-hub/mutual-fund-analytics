import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Ensure return columns are numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check invalid expense ratio
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Invalid Expense Ratio Records:", len(invalid_expense))

# Check missing values after conversion
print("\nMissing Return Values:")
print(df[return_columns].isnull().sum())

# Save cleaned file
df.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("\nScheme performance cleaned successfully!")