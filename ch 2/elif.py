"""
Module: elif.py
Purpose: Determine user eligibility based on age categories.
Description: Uses multiple elif conditions to categorize age ranges
             and provide eligibility status. (Note: Some logic may be incorrect)
"""

# Get age input from user
age = int(input("enter age: "))

# Check different age ranges and provide corresponding message
if age > 18:
    print("you are eligible for license")
elif age > 18 and age < 30:  # Note: First condition already checked age > 18, so this is unreachable
    print("you are an adult and eligible")
elif age > 30 and age < 50:  # Unreachable due to first condition
    print("warning message")
elif age < 50 and age > 100:  # Logically impossible: can't be < 50 AND > 100
    print("different message")
else:
    # Handles age <= 18
    print("you are not eligible")
    