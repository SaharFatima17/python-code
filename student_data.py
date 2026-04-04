import pandas as pd

# Load CSV file
df = pd.read_csv("students.csv")

print("Student Data:")
print(df)

# Average marks per subject
print("\nAverage marks per subject:")
print(df.mean(numeric_only=True))

# Calculate total marks
df["Total"] = df[["Math", "English", "Science"]].sum(axis=1)

# Top 3 students
print("\nTop 3 students:")
print(df.sort_values(by="Total", ascending=False).head(3))

# Students who need improvement (<50)
print("\nStudents who need improvement:")
print(df[(df["Math"] < 50) | (df["English"] < 50) | (df["Science"] < 50)])
