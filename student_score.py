students = {}

def add_student(name, score):
    students[name] = score
    with open("students.txt", "a") as file:
        file.write(f"{name}: {score}\n")
    print("Student record added!")

def calculate_average():
    if not students:
        return 0
    return sum(students.values()) / len(students)

# Example usage:
add_student("Riya", 88)
add_student("Sam", 92)
add_student("Karan", 75)

avg = calculate_average()
print(f"Class Average Score: {avg}")
