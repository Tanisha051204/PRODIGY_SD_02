import random
import sys

print("Welcome to the Guessing Game!")

lower_bound = 1
upper_bound = 100
random_number = random.randint(lower_bound, upper_bound)

attempts = 0
user_guess = None

while user_guess != random_number:
    try:
        user_guess = int(input(f"I have selected a number between {lower_bound} and {upper_bound}. Try to guess it: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    attempts += 1

    if user_guess < random_number:
        print("Too low! Try again.")
    elif user_guess > random_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")

