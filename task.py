import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

plt.scatter(df["hours_studied"], df["exam_score"])

plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Hours vs Marks")

plt.savefig("graph.png")
plt.show()