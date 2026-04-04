import numpy as np

# Marks of 5 students in 3 subjects
marks = np.array([
    [78, 85, 90],
    [65, 70, 72],
    [88, 92, 95],
    [40, 55, 60],
    [75, 80, 85]
])

# Average marks of each student
student_avg = marks.mean(axis=1)
print("Average marks of each student:")
print(student_avg)

# Highest marks in each subject
highest_subject = marks.max(axis=0)
print("\nHighest marks in each subject:")
print(highest_subject)

# Overall class average
class_avg = marks.mean()
print("\nOverall class average:")
print(class_avg)
