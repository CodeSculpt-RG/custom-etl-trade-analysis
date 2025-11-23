Custom ETL Trade Analysis Pipeline
This project implements a modularized Extract, Transform, and Load (ETL) pipeline in Python to process raw international trade data, perform feature engineering, and execute macro- and micro-level SQL analyses. The processed data is prepared for business intelligence (BI) dashboarding.

Repository Link: https://github.com/CodeSculpt-RG/custom-etl-trade-analysis

🚀 Project Structure
The repository adheres to a standard data science project structure, separating code, notebooks, data, and SQL queries:

siddharth_trade_pipeline/
├─ data/
│  ├─ raw/                  # Source data (e.g., Sample Data 2.xlsx)
│  └─ processed/            # Cleaned CSV output (trade_cleaned.csv)
├─ results/                 # Automated output of the SQL analysis (CSV tables)
├─ notebooks/               # Jupyter notebooks for exploration and validation
├─ src/                     # Modular Python code for the ETL logic
│  ├─ parsing/
│  ├─ cleaning/
│  ├─ feature_engineering/
├─ sql/                     # Dedicated SQL queries for analysis tasks
├─ dashboards/              # Placeholder for final BI outputs
├─ docs/                    # Project documentation
├─ run_pipeline.py          # Main script to run the full ETL process
└─ run_sql_analysis.py      # Script to run all SQL queries and save results
🛠️ Setup and Installation
1. Prerequisites
You must have Python (3.7+) installed. This project relies on standard data science libraries.

2. Install Dependencies
Install the required Python packages using pip:

Bash

pip install pandas openpyxl sqlite3
(Note: sqlite3 is often included with Python, but pandas and openpyxl are required for data manipulation and Excel reading.)

3. Place Raw Data
Place your source Excel file, Sample Data 2.xlsx, into the data/raw/ directory.

🏃 Running the Pipeline
The project is executed in two primary phases: data processing and data analysis.

Phase 1: Data Processing (ETL)
This script loads the raw Excel file, standardizes column names, cleans date and unit fields, extracts features using Regex (parse_goods_description.py), and calculates micro-economic features.

Run this script from the project root directory:

Bash

python run_pipeline.py
Output: A clean CSV file, trade_cleaned.csv, will be generated in data/processed/.

Phase 2: SQL Analysis
This script loads the trade_cleaned.csv into an in-memory SQLite database and executes the four required analytical SQL queries (macro_trends.sql, pareto_hsn.sql, etc.) using the Pandas read_sql_query function.

Run this script from the project root directory:

Bash

python run_sql_analysis.py
Output: Four final analytical tables will be saved as separate CSV files in the new results/ directory, ready for reporting.

📝 Analysis Outputs (Generated Files)
The results/ folder contains the final deliverables for the assignment's analytical tasks:

macro_trends_output.csv: Year-over-Year (YoY) Growth for total trade value.

pareto_hsn_output.csv: Top 25 HSN Codes by value and their contribution percentage.

supplier_analysis_output.csv: Supplier classification (Active vs. Churned).

micro_trends_output.csv: Average landed cost and duty anomaly count per product model.

These outputs confirm the successful execution of all cleaning, feature engineering, and SQL analysis tasks.
