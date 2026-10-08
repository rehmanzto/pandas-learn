import pandas as pd
import numpy as np

print("=== 07: Data Cleaning ===\n")

df = pd.DataFrame({
    "name": ["Ashiq", "Rahim", "Karim", "Nadia", "Ashiq", None],
    "age": [21, 22, np.nan, 21, 21, 20],
    "score": [92, 85, 78, np.nan, 92, 67],
    "city": ["Dhaka", "Chittagong", "Dhaka", None, "Dhaka", "Rajshahi"],
})

print("Dirty data:")
print(df)

print("\nMissing values per column:")
print(df.isna().sum())

# Fill missing numeric values
df["age"] = df["age"].fillna(df["age"].mean())
df["score"] = df["score"].fillna(df["score"].mean())

# Fill missing text
df["city"] = df["city"].fillna("Unknown")
df["name"] = df["name"].fillna("Unknown")

print("\nAfter filling missing values:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

print("\nAfter removing duplicate rows:")
print(df)

# Rename a column
df = df.rename(columns={"score": "exam_score"})

# Convert type
df["age"] = df["age"].round().astype(int)

print("\nAfter rename/type cleanup:")
print(df)

# Basic validation
print("\nFinal missing values:")
print(df.isna().sum())

print("\nFinal data:")
print(df)
