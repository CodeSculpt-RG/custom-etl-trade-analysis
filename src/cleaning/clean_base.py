import pandas as pd

def clean_data(df):
    # --- 1. Robust Column Standardization ---
    # Convert to lowercase, replace spaces with underscores, and strip edges
    def standardize_cols(col_name):
        return col_name.strip().lower().replace(' ', '_').replace('.', '_').replace('-', '_').replace('(', '').replace(')', '')

    df.columns = [standardize_cols(col) for col in df.columns]
    
    # --- 2. Date Fix (Column should now be named 'date') ---
    if 'date' in df.columns:
        df.rename(columns={'date': 'date_of_shipment'}, inplace=True)
    elif 'date_of_shipment' not in df.columns:
        # Fallback if standardization wasn't enough
        raise KeyError("Could not find a valid date column (looking for 'date_of_shipment' or 'date').")
    
    df['date_of_shipment'] = pd.to_datetime(df['date_of_shipment'], errors='coerce')
    df['year'] = df['date_of_shipment'].dt.year
    df['month'] = df['date_of_shipment'].dt.month
    
    # --- 3. Unit Standardization (Column should now be named 'unit') ---
    if 'unit' in df.columns:
        unit_map = {
            'nos': 'PCS', 'no': 'PCS', 'pieces': 'PCS', 'piece': 'PCS', 'pcs': 'PCS',
            'kgs': 'KG', 'kg': 'KG', 'mt': 'MT', 'set': 'SET'
        }
        df['unit_standardized'] = df['unit'].str.lower().str.strip().map(unit_map).fillna('OTHER')
    else:
        df['unit_standardized'] = 'UNKNOWN'

    return df