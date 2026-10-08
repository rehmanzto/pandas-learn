import pandas as pd
from pathlib import Path

print("=== 08: Mini Project — Student Data Analysis ===\n")

BASE = Path(__file__).resolve().parents[1]
csv_path = BASE / "data" / "students.csv"

# 1. Load
df = pd.read_csv(csv_path)

# 2. Inspect
print("DATA")
print(df)
print("\nShape:", df.shape)

# 3. Clean
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["score"] = df["score"].fillna(df["score"].mean())
df["city"] = df["city"].fillna("Unknown")
df = df.drop_duplicates()

# 4. Create useful columns
df["passed"] = df["score"] >= 40
df["grade"] = pd.cut(
    df["score"],
    bins=[0, 39, 49, 59, 69, 79, 89, 100],
    labels=["F", "D", "C", "B", "B+", "A", "A+"],
)

# 5. Filter
top_students = df[df["score"] >= 90].sort_values("score", ascending=False)

print("\nTOP STUDENTS")
print(top_students[["name", "department", "score", "grade"]])

# 6. Aggregate
department_summary = df.groupby("department").agg(
    average_score=("score", "mean"),
    students=("name", "count"),
    highest_score=("score", "max"),
)

print("\nDEPARTMENT SUMMARY")
print(department_summary.sort_values("average_score", ascending=False))

# 7. Export final dataset
output_path = BASE / "data" / "students_analyzed.csv"
df.to_csv(output_path, index=False)

print(f"\nAnalyzed dataset saved to:\n{output_path}")
