"""
Number Reversal Program

Reverses the digits of an integer entered by the user.
Example: 12345 becomes 54321
"""

# Take integer input from the user
b = int(input("Enter number: "))

# Initialize reversed number accumulator
rev = 0

# Extract digits from right to left and build the reversed number
while b > 0:
    # Shift rev left by one digit and add the last digit of b
    rev = rev * 10 + b % 10
    
    # Remove the last digit from b
    b = b // 10

# Display the reversed number
print(rev)
