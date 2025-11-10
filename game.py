import random

score = 0  # keeps track of total score
print(" Welcome to the Guess the Number Game!")

while True:
    number = random.randint(1, 10) #random integer from 1 to 10
    attempts = 0
    guessed = False

    print("\nI'm thinking of a number between 1 and 10.")
    print("You have 3 attempts to guess it!")

    while attempts < 3:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number:
            print(" Correct! You guessed it!")
            score += 1
            guessed = True
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

    if not guessed:
        print(f" Out of attempts! The correct number was {number}.")

    print(f"Your current score: {score}")
    break
