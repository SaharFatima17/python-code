# Even or Odd Checker
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Positive, Negative, or Zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Simple Login Check
password = "python123"
user_input = input("Enter password: ")
if user_input == password:
    print("Access Granted")
else:
    print("Access Denied")



# Basic Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")

# Age Category Finder
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

# Number Guessing Game
secret_number = 7
guess = None
while guess != secret_number:
    guess = int(input("Guess the number: "))
    if guess != secret_number:
        print("Try again!")
print("Correct!")




# Login Attempt System
correct_username = "admin"
correct_password = "pass123"
attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        attempts -= 1
        print(f"Incorrect! {attempts} attempt(s) left.")
else:
    print("Account Locked")

# Menu-Driven ATM Simulator
balance = 10000
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        print(f"Your balance is: {balance}")
    elif choice == '2':
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Money deposited successfully.")
    elif choice == '3':
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Money withdrawn successfully.")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print("Thank you for using our ATM!")
        break
    else:
        print("Invalid choice!")

# Multiplication Table Generator
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# Password Strength Checker
password = input("Enter a password: ")

has_number = False
has_upper = False

for char in password:
    if char.isdigit():
        has_number = True
    if char.isupper():
        has_upper = True

if len(password) >= 8 and has_number and has_upper:
    print("Strong Password")
else:
    print("Weak Password")
