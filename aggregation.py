import pandas as pd

print("=== 06: Aggregation ===\n")

df = pd.DataFrame({
    "name": ["Ashiq", "Rahim", "Karim", "Nadia", "Sami", "Mim", "Rafi"],
    "department": ["CSE", "EEE", "CSE", "BBA", "CSE", "EEE", "BBA"],
    "score": [92, 85, 78, 88, 95, 67, 73],
    "age": [21, 22, 20, 21, 23, 20, 22],
})

print("Data:")
print(df)

print("\nOverall mean score:")
print(df["score"].mean())

print("\nOverall max score:")
print(df["score"].max())

print("\nOverall min score:")
print(df["score"].min())

print("\nNumber of students:")
print(df["name"].count())

print("\nMean score by department:")
print(df.groupby("department")["score"].mean())

print("\nMultiple aggregations by department:")
summary = df.groupby("department").agg(
    average_score=("score", "mean"),
    highest_score=("score", "max"),
    lowest_score=("score", "min"),
    students=("name", "count"),
)
print(summary)

print("\nSorted summary:")
print(summary.sort_values("average_score", ascending=False))
