import os

folders = [
    "src",
    "src/cleaning",
    "src/parsing",
    "src/feature_engineering",
    "src/db"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    
    file_path = os.path.join(folder, "__init__.py")
    
    with open(file_path, "w") as f:
        pass 
        
    print(f"✅ Created: {file_path}")

print("\nAll folders are now valid Python packages!")