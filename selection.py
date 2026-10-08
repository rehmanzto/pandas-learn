import pandas as pd

print("=== 04: Selection ===\n")

df = pd.DataFrame({
    "name": ["Ashiq", "Rahim", "Karim", "Nadia", "Sami"],
    "age": [21, 22, 20, 21, 23],
    "department": ["CSE", "EEE", "CSE", "BBA", "CSE"],
    "score": [92, 85, 78, 88, 95],
})

print("Original:")
print(df)

print("\nOne column:")
print(df["name"])

print("\nMultiple columns:")
print(df[["name", "score"]])

print("\nFirst row with iloc:")
print(df.iloc[0])

print("\nFirst 3 rows with iloc:")
print(df.iloc[:3])

print("\nRow 2, score column:")
print(df.iloc[2]["score"])

print("\nRows 1-3 and selected columns with loc:")
print(df.loc[1:3, ["name", "score"]])

# Select using a condition
print("\nCSE students:")
print(df.loc[df["department"] == "CSE", ["name", "score"]])
