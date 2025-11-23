import os

def create_structure():
    structure = {
        "data/raw": [],
        "data/processed": [],
        "notebooks": [
            "01_data_inspection.ipynb",
            "02_parsing_and_cleaning.ipynb",
            "03_feature_engineering.ipynb"
        ],
        "src/parsing": ["parse_goods_description.py"],
        "src/cleaning": ["clean_base.py"],
        "src/feature_engineering": ["features.py"],
        "src/db": ["load_to_db.py"],
        "sql": [
            "schema.sql",
            "macro_trends.sql",
            "pareto_hsn.sql",
            "supplier_analysis.sql"
        ],
        "dashboards/exports": [],
        "docs": []
    }

    base_path = os.getcwd()

    for folder, files in structure.items():
        dir_path = os.path.join(base_path, folder)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created folder: {folder}")

        
        for file in files:
            file_path = os.path.join(dir_path, file)
            with open(file_path, 'w') as f:
                pass  
            print(f"  Created file: {file}")

if __name__ == "__main__":
    create_structure()