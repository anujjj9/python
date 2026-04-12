"""
Character Classification Counter

This module counts the number of digits, alphabetic characters, and special 
characters in a given string.
"""

a = "GF%&HH***^^BHH"
dig = 0          # Counter for digits
char = 0         # Counter for alphabetic characters
spchar = 0       # Counter for special characters

# Iterate through each character in the string
for i in a:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        char += 1
    else:
        # Any character that is neither digit nor letter
        spchar += 1

print(f"digit is {dig} , char is {char} and special char is {spchar}")