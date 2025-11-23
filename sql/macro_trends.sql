-- Query to calculate YoY Growth for Grand Total
WITH YearlyTotals AS (
    -- 1. Aggregate Grand Total by Year
    SELECT
        year,
        SUM(grand_total) AS current_year_total
    FROM trade_cleaned
    GROUP BY year
),
YoYCalculations AS (
    -- 2. Use LAG window function to get the previous year's total
    SELECT
        year,
        current_year_total,
        LAG(current_year_total, 1) OVER (ORDER BY year) AS previous_year_total
    FROM YearlyTotals
)
-- 3. Calculate YoY Growth Percentage
SELECT
    year,
    current_year_total,
    previous_year_total,
    -- Calculate YoY Growth Percentage (rounded)
    ROUND(((current_year_total - previous_year_total) * 100.0) / previous_year_total, 2) AS yoy_grand_total_growth_pct
FROM YoYCalculations
WHERE previous_year_total IS NOT NULL
ORDER BY year;