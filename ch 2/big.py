"""
Module: big.py
Purpose: Compare two numbers and determine which is larger.
Description: Takes two integer inputs from user and outputs 
             the larger of the two numbers.
"""

# Prompt and input the first number from user
a = int(input("enter first number: "))

# Prompt and input the second number from user
b = int(input("enter second number: "))  # Note: prompt says "first" but should be "second"

# Compare and display the larger number
if a > b: 
    print("a is largest")
else: 
    print("b is largest")
    
