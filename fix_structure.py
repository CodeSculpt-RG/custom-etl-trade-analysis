import os

# The folders that need the init file
folders = [
    "src",
    "src/cleaning",
    "src/parsing",
    "src/feature_engineering",
    "src/db"
]

for folder in folders:
    # 1. Ensure the folder actually exists
    os.makedirs(folder, exist_ok=True)
    
    # 2. Define the file path
    file_path = os.path.join(folder, "__init__.py")
    
    # 3. Create the empty file
    with open(file_path, "w") as f:
        pass # Just create it and do nothing
        
    print(f"✅ Created: {file_path}")

print("\nAll folders are now valid Python packages!")