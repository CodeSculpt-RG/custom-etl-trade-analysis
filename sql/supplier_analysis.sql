-- Query to identify supplier longevity (Active vs. Churned)
WITH SupplierActivity AS (
    -- Assuming 'iec' serves as a unique supplier identifier
    SELECT 
        iec,
        MAX(year) AS last_active_year,
        SUM(total_value_inr) AS lifetime_value
    FROM trade_cleaned
    GROUP BY iec
)
SELECT 
    iec,
    last_active_year,
    lifetime_value,
    CASE 
        -- Assuming 2025 is the latest year in the data
        WHEN last_active_year = 2025 THEN 'Active (Current)'
        ELSE 'Churned/Historical' 
    END AS supplier_status
FROM SupplierActivity
ORDER BY lifetime_value DESC;