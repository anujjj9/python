"""
Factorial Calculator

Computes the factorial of a given number n (n!).
Factorial is the product of all positive integers from 1 to n.
"""

n = int(input("enter number:"))
fact = 1  # Variable to store the factorial result

# Multiply all numbers from 1 to n
for i in range(1, n + 1):
    fact = fact * i

print(f" factorial is {fact}")