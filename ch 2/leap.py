"""
Module: leap.py
Purpose: Determine if a given year is a leap year.
Description: Uses the leap year rules:
             - Divisible by 4 AND not by 100, OR
             - Divisible by 400
"""

# Get year input from user
n = int(input("enter year: "))  # Fixed: remove print() from input()

# Check leap year conditions
if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print("leap year")
else:
    print("this is not a leap year")