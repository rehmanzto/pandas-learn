import pandas as pd

print("=== 05: Filtering ===\n")

df = pd.DataFrame({
    "name": ["Ashiq", "Rahim", "Karim", "Nadia", "Sami", "Mim"],
    "age": [21, 22, 20, 21, 23, 20],
    "department": ["CSE", "EEE", "CSE", "BBA", "CSE", "EEE"],
    "score": [92, 85, 78, 88, 95, 67],
})

print("Original:")
print(df)

# One condition
print("\nScore >= 80:")
print(df[df["score"] >= 80])

# Text condition
print("\nCSE only:")
print(df[df["department"] == "CSE"])

# AND condition
print("\nCSE AND score >= 90:")
print(df[(df["department"] == "CSE") & (df["score"] >= 90)])

# OR condition
print("\nCSE OR EEE:")
print(df[df["department"].isin(["CSE", "EEE"])])

# NOT condition
print("\nNot CSE:")
print(df[df["department"] != "CSE"])

# String filtering
print("\nNames starting with A:")
print(df[df["name"].str.startswith("A")])

# Sorting after filtering
print("\nScore >= 80, sorted highest first:")
result = df[df["score"] >= 80].sort_values("score", ascending=False)
print(result)
