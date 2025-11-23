import pandas as pd
import sys
import os

# --- PART 1: AUTO-REPAIR STRUCTURE (for __init__.py files) ---
project_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(project_root, 'src')

required_init_folders = [
    src_path,
    os.path.join(src_path, 'cleaning'),
    os.path.join(src_path, 'parsing'),
    os.path.join(src_path, 'feature_engineering'),
    os.path.join(src_path, 'db')
]

print("--- Checking Project Structure ---")
for folder in required_init_folders:
    if os.path.exists(folder):
        init_file = os.path.join(folder, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f: pass
            print(f"Fixed: Created missing file -> {init_file}")
    else:
        print(f"WARNING: Folder missing -> {folder}")

# --- PART 2: PACKAGE IMPORTS ---

# Add the project root to path so we can import 'src'
if project_root not in sys.path:
    sys.path.append(project_root)

try:
    from src.cleaning.clean_base import clean_data
    from src.parsing.parse_goods_description import parse_description
    from src.feature_engineering.features import add_features
    print("✅ Imports successful!")
except ImportError as e:
    print(f"\n❌ CRITICAL ERROR: {e}")
    sys.exit(1)

# --- PART 3: MAIN PIPELINE EXECUTION ---

def main():
    print("--- Starting Pipeline Processing ---")
    
    # 1. Load Data
    raw_path = os.path.join(project_root, 'data', 'raw', 'Sample Data 2.xlsx')
    
    if not os.path.exists(raw_path):
        print(f"❌ ERROR: Input file not found: {raw_path}")
        return

    df = pd.read_excel(raw_path)
    print(f"Data loaded: {len(df)} rows")

    # 2. Clean (Standardizes column names to snake_case here)
    df = clean_data(df)
    print("Basic cleaning and column standardization complete.")

    # 3. Parse Text
    print("Parsing descriptions (Regex)...")
    # FIX: Renaming output columns to snake_case to prevent SQL duplicate column error
    df[['model_name_parsed', 'capacity_spec_parsed', 'material_type_parsed', 'embedded_qty_parsed', 'unit_price_usd_parsed']] = \
        df['goods_description'].apply(parse_description)

    # 4. Feature Engineering (Creates grand_total, categories, and anomaly flags)
    df = add_features(df)
    print("Feature engineering complete.")

    # 5. Save Output
    output_path = os.path.join(project_root, 'data', 'processed', 'trade_cleaned.csv')
    
    # Ensure the directory exists before saving
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)
    
    df.to_csv(output_path, index=False)
    print(f"✅ SUCCESS! Pipeline finished. Data saved to: {output_path}")

if __name__ == "__main__":
    main()