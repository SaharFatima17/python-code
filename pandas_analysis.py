import pandas as pd

# Create DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Usman"],
    "Age": [20, 21, 22, 20, 23],
    "Marks": [78, 45, 88, 60, 49]
}

df = pd.DataFrame(data)
print(df)

# Average marks
avg_marks = df["Marks"].mean()

# Students scoring above average
print("\nStudents scoring above average:")
print(df[df["Marks"] > avg_marks])

# Add Result column
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print("\nUpdated DataFrame:")
print(df)
