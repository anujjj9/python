"""
Module: gender.py
Purpose: Greet users with gender-specific salutation.
Description: Takes gender input (m/f) and displays appropriate greeting.
"""

# Prompt user to enter gender
gender = input("enter m for male and f for female: ")

# Display greeting based on gender
if gender == "m":
    print("hello sir")
elif gender == "f":
    print("hello madam")
else:
    # Handle invalid inputs
    print("Invalid input")