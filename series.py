import pandas as pd

print("=== 01: Pandas Series ===\n")

# A Series is a one-dimensional labeled data structure.
scores = pd.Series([92, 85, 78, 88, 95])
print("Series:")
print(scores)

# Custom index
scores = pd.Series(
    [92, 85, 78],
    index=["Ashiq", "Rahim", "Karim"],
    name="Score"
)

print("\nCustom index:")
print(scores)

print("\nSingle value:")
print(scores["Ashiq"])

print("\nMultiple values:")
print(scores[["Ashiq", "Karim"]])

print("\nSeries values:")
print(scores.values)

print("\nSeries index:")
print(scores.index)

print("\nBasic statistics:")
print("Mean:", scores.mean())
print("Max:", scores.max())
print("Min:", scores.min())

print("\nBoolean comparison:")
print(scores > 80)
