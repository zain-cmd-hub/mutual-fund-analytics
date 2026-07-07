-- Query 1: Top 5 Funds by AUM

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Query 2: Average NAV Per Month

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- Query 3: SIP Transactions Year-wise

SELECT
    strftime('%Y', transaction_date) AS year,
    COUNT(*) AS total_sip_transactions,
    SUM(amount_inr) AS total_sip_amount
FROM investor_transactions
WHERE transaction_type = 'Sip'
GROUP BY year
ORDER BY year;

-- Query 4: Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- Query 5: Funds with Expense Ratio Less Than 1%

SELECT
    scheme_name,
    fund_house,
    category,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct ASC;

-- Query 6: Top 5 Funds by 1-Year Return

SELECT
    scheme_name,
    fund_house,
    return_1yr_pct
FROM scheme_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- Query 7: Transactions by Payment Mode

SELECT
    payment_mode,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY payment_mode
ORDER BY total_transactions DESC;

-- Query 8: Average Return by Category

SELECT
    category,
    ROUND(AVG(return_1yr_pct),2) AS avg_return
FROM scheme_performance
GROUP BY category;

-- Query 9: Transactions by KYC Status

SELECT
    kyc_status,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY kyc_status;

-- Query 10: Highest NAV Recorded

SELECT
    amfi_code,
    MAX(nav) AS highest_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY highest_nav DESC
LIMIT 5;