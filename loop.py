#loop in str
name="Hello"   
print(name)
for i in name:
    print(i)

#range  start from specific number
for i in range(10,101):
    print(i)

#gaping
for i in range(10,101,2):   #gap of 2
    print(i)


#print * in reverse
for i in range(6,1,-1):
    print("*" * i)


# Example 12: Star Pattern
for i in range(1, 6):
    print("*" * i)


# Example 13: Multiplication Table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# Example 14: Sum of 5 Numbers
total = 0

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    total += num

print("Sum of numbers:", total)


# Example 15: Loading Bar Animation
import time

for i in range(1, 11):
    print("Loading" + "." * i)
    time.sleep(0.3)  # small pause



# Using a for loop
print("Using for loop:")
for i in range(1, 11):
    print(i)

# Using a while loop
print("\nUsing while loop:")
i = 1
while i <= 10:
    print(i)
    i += 1

#even number from 2 to 20
for i in range(2, 21, 2):
    print(i)



for i in range(1, 11):
    if i == 5:
        continue     # skip 5
    if i == 8:
        break         # stop loop when number is 8
    print(i)
