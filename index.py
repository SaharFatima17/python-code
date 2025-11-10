class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.m1 = marks1
        self.m2 = marks2
        self.m3 = marks3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def show(self):
        print("Name:", self.name)
        print("Average Marks:", self.average())


# Example:
s1 = Student("Ali", 80, 90, 85)
s1.show()

s2 = Student("Sara", 75, 88, 92)
s2.show()
