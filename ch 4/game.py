"""
Number Guessing Game

A simple interactive game where the user guesses a randomly generated number.
The program provides hints to guide the user towards the correct answer.
"""

import random

# Generate a random number between 1 and 11 for the user to guess
num = random.randint(1, 11)

# Counter to track the number of guesses made by the user
tries = 0

# Main game loop that continues until the correct number is guessed
while True:
    # Get user input for their guess
    guess = int(input("Please guess the number: "))
    
    # Increment tries counter with each guess
    tries += 1
    
    # Check if the guess is correct
    if num == guess:
        print(f"You're right! You guessed it in {tries} tries.")
        break
    # Provide hint if guess is too large
    elif num < guess:
        print("Go smaller.")
    # Provide hint if guess is too small
    elif num > guess:
        print("Go bigger.")