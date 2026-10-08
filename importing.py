import pandas as pd
from pathlib import Path

print("=== 03: Importing & Exporting Data ===\n")

BASE = Path(__file__).resolve().parents[1]
csv_path = BASE / "data" / "students.csv"

# Read CSV
df = pd.read_csv(csv_path)

print("CSV data:")
print(df)

# Useful import options
# pd.read_csv("file.csv", nrows=5)
# pd.read_csv("file.csv", usecols=["name", "score"])

# Export CSV
output_path = BASE / "data" / "students_copy.csv"
df.to_csv(output_path, index=False)
print(f"\nSaved CSV to: {output_path}")

# JSON example
json_path = BASE / "data" / "students.json"
df.to_json(json_path, orient="records", indent=2)
print(f"Saved JSON to: {json_path}")

# Read JSON
json_df = pd.read_json(json_path)
print("\nRead back from JSON:")
print(json_df)

# Excel support requires openpyxl
excel_path = BASE / "data" / "students.xlsx"
df.to_excel(excel_path, index=False)
print(f"\nSaved Excel to: {excel_path}")

excel_df = pd.read_excel(excel_path)
print("\nRead back from Excel:")
print(excel_df)
