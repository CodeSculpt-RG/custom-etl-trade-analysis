-- Query to perform Pareto Analysis (Top 25 vs. Others)
WITH HSN_Totals AS (
    -- 1. Calculate Total Value for each HSN Code
    SELECT 
        hsn_code,
        SUM(grand_total) AS total_hsn_value
    FROM trade_cleaned
    GROUP BY hsn_code
),
HSN_Ranked AS (
    -- 2. Rank HSN Codes by value and calculate the total market size
    SELECT 
        hsn_code,
        total_hsn_value,
        ROW_NUMBER() OVER (ORDER BY total_hsn_value DESC) AS rank_num,
        SUM(total_hsn_value) OVER () AS total_market_value
    FROM HSN_Totals
),
Top25 AS (
    -- 3. Select the Top 25 Codes
    SELECT 
        hsn_code,
        total_hsn_value,
        (total_hsn_value * 100.0 / total_market_value) AS contribution_pct,
        'Top 25' AS type
    FROM HSN_Ranked
    WHERE rank_num <= 25
),
Others AS (
    -- 4. Aggregate all remaining codes into "Others"
    SELECT 
        'Others' AS hsn_code,
        SUM(total_hsn_value) AS total_hsn_value,
        SUM(total_hsn_value * 100.0 / total_market_value) AS contribution_pct,
        'Others' AS type
    FROM HSN_Ranked
    WHERE rank_num > 25
)
-- 5. Combine the results
SELECT hsn_code, total_hsn_value, ROUND(contribution_pct, 2) AS contribution_pct, type
FROM Top25
UNION ALL
SELECT hsn_code, total_hsn_value, ROUND(contribution_pct, 2) AS contribution_pct, type
FROM Others
ORDER BY total_hsn_value DESC;