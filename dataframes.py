import pandas as pd

print("=== 02: Pandas DataFrames ===\n")

# DataFrame = table made from rows and columns.
data = {
    "name": ["Ashiq", "Rahim", "Karim", "Nadia"],
    "age": [21, 22, 20, 21],
    "department": ["CSE", "EEE", "CSE", "BBA"],
    "score": [92, 85, 78, 88],
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nShape (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nFirst 2 rows:")
print(df.head(2))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nInformation:")
df.info()

print("\nStatistics:")
print(df.describe(numeric_only=True))

# Add a new column
df["passed"] = df["score"] >= 40

print("\nAfter adding 'passed':")
print(df)
