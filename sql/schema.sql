-- Use DROP TABLE IF EXISTS if your database supports it (e.g., SQLite, MySQL, PostgreSQL)
-- If running on SQL Server (T-SQL), you would need a different conditional block.
-- For universal compatibility, we simplify the CREATE statement:

CREATE TABLE trade_cleaned (
    port_code TEXT,
    date_of_shipment DATE,
    iec TEXT,
    hs_code INTEGER,
    goods_description TEXT,
    master_category TEXT,
    model_name TEXT,
    model_number TEXT,
    capacity TEXT,
    qty REAL,
    unit_of_measure TEXT,
    price REAL,
    unit_of_measure_1 TEXT,
    quantity REAL,
    unit TEXT,
    unit_price_inr REAL,
    total_value_inr REAL,
    unit_price_usd REAL,
    total_value_usd REAL,
    duty_paid_inr REAL,
    -- Generated Columns
    year INTEGER,
    month INTEGER,
    unit_standardized TEXT,
    model_name_parsed TEXT,
    capacity_spec TEXT,
    material_type TEXT,
    embedded_qty INTEGER,
    unit_price_usd_parsed REAL,
    grand_total REAL,
    landed_cost_per_unit REAL,
    category TEXT,
    sub_category TEXT,
    duty_pct REAL,
    is_duty_anomaly TEXT
);