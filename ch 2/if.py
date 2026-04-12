"""
Module: if.py
Purpose: Determine if a number is even or odd.
Description: Takes an integer input and checks divisibility by 2
             to classify as even or odd.
"""

# Get an integer input from user
a = int(input("enter a number: "))

# Check divisibility by 2 to determine even or odd
if a % 2 == 0: 
    print("even")
else: 
    print("odd")