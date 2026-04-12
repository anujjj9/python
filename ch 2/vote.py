"""
Module: vote.py
Purpose: Check voting eligibility based on age.
Description: Determines if a person is eligible to vote (age 18+)
             and displays personalized message.
"""

# Get name and age from user
name = input("enter name: ")  # Fixed: remove print() from input()
age = int(input("enter age: "))

# Check voting eligibility
if age >= 18:  # Changed from > to >=
    print(f"hello {name}, you are eligible to vote")
else:
    print(f"hello {name}, you are not eligible")  # Fixed typo: "ure" → "you are"