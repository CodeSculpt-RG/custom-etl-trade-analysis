import pandas as pd
import numpy as np

def add_features(df):
    
    # FIX: Rename 'hs_code' to 'hsn_code' to match documentation requirements
    if 'hs_code' in df.columns and 'hsn_code' not in df.columns:
        df.rename(columns={'hs_code': 'hsn_code'}, inplace=True)
        
    # Ensure necessary columns exist before proceeding
    required_cols = ['total_value_inr', 'duty_paid_inr', 'quantity', 'hsn_code', 'goods_description']
    for col in required_cols:
        if col not in df.columns:
            print(f"❌ Feature Engineering Error: Missing required column '{col}'. Available columns: {df.columns.tolist()}")
            # Create a placeholder column to avoid crashing if absolutely necessary
            df[col] = 0

    # Grand Total (Task 2)
    df['grand_total'] = df['total_value_inr'] + df['duty_paid_inr']
    
    # Landed Cost Per Unit (Task 4)
    df['landed_cost_per_unit'] = df.apply(
        lambda x: x['grand_total'] / x['quantity'] if x['quantity'] > 0 else 0, axis=1
    )
    
    # Categorization Logic (Task 2)
    def get_category(row):
        hsn = str(row['hsn_code'])
        desc = str(row['goods_description']).upper()
        
        if 'GLASS' in desc or hsn.startswith('70'):
            return 'Glassware', 'Borosilicate' if 'BOROSILICATE' in desc else 'General Glass'
        elif 'WOOD' in desc or hsn.startswith('44'):
            return 'Woodenware', 'Kitchen' if 'SPOON' in desc else 'Furniture'
        elif 'ELEC' in desc or hsn.startswith('85'):
            return 'Electronics', 'Components'
        else:
            return 'Other', 'General'

    df[['category', 'sub_category']] = df.apply(lambda x: pd.Series(get_category(x)), axis=1)

    # Unit Economics & Anomaly Detection (Task 4)
    df['duty_pct'] = df['duty_paid_inr'] / df['total_value_inr']
    
    # Flag Anomalies if outside 2 Standard Deviations
    # Note: Calculate mean/std only for valid duty percentages (not infinity or NaN)
    valid_duty_pct = df['duty_pct'].replace([np.inf, -np.inf], np.nan).dropna()
    if not valid_duty_pct.empty:
        mean_duty = valid_duty_pct.mean()
        std_duty = valid_duty_pct.std()
        
        df['is_duty_anomaly'] = df['duty_pct'].apply(
            lambda x: 'Yes' if (x > mean_duty + 2*std_duty) or (x < mean_duty - 2*std_duty) else 'No'
        )
    else:
        df['is_duty_anomaly'] = 'No' # Default if no data to calculate
    
    return df