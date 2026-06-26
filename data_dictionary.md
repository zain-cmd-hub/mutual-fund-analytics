# Data Dictionary

## Dataset: nav_history

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value of the scheme |

Source: 02_nav_history.csv

---

## Dataset: investor_transactions

| Column | Data Type | Description |
|--------|-----------|-------------|
| investor_id | Text | Unique investor ID |
| transaction_date | Date | Date of transaction |
| amfi_code | Integer | Mutual fund scheme code |
| transaction_type | Text | SIP, Lumpsum or Redemption |
| amount_inr | Integer | Transaction amount in INR |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | Tier classification |
| age_group | Text | Investor age group |
| gender | Text | Investor gender |
| annual_income_lakh | Float | Annual income (Lakhs) |
| payment_mode | Text | Mode of payment |
| kyc_status | Text | KYC verification status |

Source: 08_investor_transactions.csv

---

## Dataset: scheme_performance

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| scheme_name | Text | Name of mutual fund scheme |
| fund_house | Text | Mutual fund company |
| category | Text | Fund category |
| plan | Text | Regular or Direct |
| return_1yr_pct | Float | One year return (%) |
| return_3yr_pct | Float | Three year return (%) |
| return_5yr_pct | Float | Five year return (%) |
| benchmark_3yr_pct | Float | Benchmark return |
| alpha | Float | Alpha value |
| beta | Float | Beta value |
| sharpe_ratio | Float | Sharpe Ratio |
| sortino_ratio | Float | Sortino Ratio |
| std_dev_ann_pct | Float | Annual Standard Deviation |
| max_drawdown_pct | Float | Maximum Drawdown |
| aum_crore | Integer | Assets Under Management (Crores) |
| expense_ratio_pct | Float | Expense Ratio (%) |
| morningstar_rating | Integer | Morningstar Rating |
| risk_grade | Text | Risk Grade |

Source: 07_scheme_performance.csv