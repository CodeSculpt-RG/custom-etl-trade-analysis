import pandas as pd
import re

def parse_description(text):
    if not isinstance(text, str):
        return pd.Series([None, None, None, None, None])
    
    text_upper = text.upper()
    
    
    model_match = re.search(r'MODEL\s*[:\-]?\s*([A-Z0-9\-]+)', text_upper)
    model = model_match.group(1) if model_match else "Unknown"
    
    
    cap_match = re.search(r'(\d+\.?\d*)\s*(ML|L|LITRE|KG|GM|INCH|MM|CM|WATT|V)', text_upper)
    capacity = f"{cap_match.group(1)}{cap_match.group(2)}" if cap_match else None
    
    material = "General"
    materials = ['GLASS', 'STEEL', 'WOOD', 'PLASTIC', 'IRON', 'CERAMIC', 'COTTON']
    for m in materials:
        if m in text_upper:
            material = m.capitalize()
            break
    
    
    qty_match = re.search(r'(?:PACK OF|QTY|QUANTITY)\s*[:\-]?\s*(\d+)', text_upper)
    embedded_qty = int(qty_match.group(1)) if qty_match else None
    
    
    price_match = re.search(r'(?:USD|US\$)\s*([\d\.]+)', text_upper)
    usd_price = float(price_match.group(1)) if price_match else None
    
    return pd.Series([model, capacity, material, embedded_qty, usd_price])