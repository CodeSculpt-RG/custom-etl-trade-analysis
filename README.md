Custom ETL Trade Analysis Pipeline 🚢

This project implements a modularized Extract, Transform, and Load (ETL) pipeline in Python to process raw international trade data, perform extensive feature engineering, and execute macro- and micro-level SQL analyses. The processed, high-value data is structured and prepared for business intelligence (BI) dashboarding.

Repository Link: https://github.com/CodeSculpt-RG/custom-etl-trade-analysis

📋 Table of Contents

Key Features & Engineering

Project Structure

Setup and Installation

Running the Pipeline

Analysis Outputs

✨ Key Features & Engineering

The strength of this pipeline lies in its ability to extract latent information and automate compliance checks before the data hits the database.

Feature

Description

Technical Implementation

Data Standardization

Handles varied casing, whitespace, and unit formats (e.g., 'kgs', 'nos') to a standard (KG, PCS).

pandas.str.strip().str.lower(), Unit Mapping in src/cleaning/clean_base.py.

Custom Data Parsing

Uses Regular Expressions (Regex) to extract granular, unstructured details (Model Name, Capacity, Material) from the free-text goods_description.

re library used in src/parsing/parse_goods_description.py.

Micro-Economic KPIs

Calculates the Landed Cost Per Unit by summing total value and duty and dividing by standardized quantity.

Feature Engineering in src/feature_engineering/features.py.

Anomaly Detection

Flags transactions where the Duty Percentage deviates by more than two standard deviations from the mean duty rate.

Statistical calculation (.std(), .mean()) in src/feature_engineering/features.py.

📂 Project Structure

The project adheres to a robust, modular architecture to separate concerns (cleaning, parsing, feature creation).

siddharth_trade_pipeline/
├── data/
│   ├── processed/          # ⬅️ Final output: trade_cleaned.csv
│   └── raw/                # ⬅️ Input: Sample Data 2.xlsx
├── results/                # ⬅️ Final Analytical Tables (CSV outputs)
├── src/
│   ├── cleaning/           # Base data standardization logic
│   ├── feature_engineering/# KPI and Anomaly calculation
│   └── parsing/            # Regex logic for Goods Description
├── sql/                    # Dedicated SQL queries for analysis (Task 3 & 4)
├── run_pipeline.py         # Executes the full ETL (Python)
└── run_sql_analysis.py     # Executes all SQL queries (Python + SQLite)


🛠️ Setup and Installation

1. Prerequisites

You must have Python 3.8+ installed.

2. Install Dependencies

Install the required Python packages:

pip install pandas openpyxl


3. Data Placement

Place your source Excel file, Sample Data 2.xlsx, into the data/raw/ directory.

🏃 Running the Pipeline

The project is executed in two simple steps from the project root directory.

Phase 1: Data Processing (ETL)

This script executes the cleaning and feature engineering logic, generating the clean CSV file.

python run_pipeline.py


Output: trade_cleaned.csv is generated in data/processed/.

Phase 2: SQL Analysis

This script loads the trade_cleaned.csv into an in-memory SQLite database and executes the four analytical SQL queries.

python run_sql_analysis.py


Output: Four analytical tables are saved as CSV files in the results/ directory.

📈 Analysis Outputs

The generated files in the results/ folder represent the final analytical deliverables:

File Name

Focus

Key Deliverable

macro_trends_output.csv

Macro Trends

Year-over-Year (YoY) Growth for total trade value.

pareto_hsn_output.csv

HSN Analysis

Top 25 HSN Codes by total value and contribution.

supplier_analysis_output.csv

Supplier Longevity

Classification of suppliers (Active vs. Churned).

micro_trends_output.csv

Micro Economics

Average landed cost and duty anomaly count per product model.
