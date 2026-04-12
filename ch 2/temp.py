"""
Module: temp.py
Purpose: Categorize temperature into different ranges.
Description: Takes a temperature value and classifies it as:
             freezing, cold, moderate, warm, or hot.
"""

# Get temperature input from user
temp = int(input("enter a temperature: "))  # Fixed: remove print() from input()

# Categorize temperature into ranges
if temp < 0:
    print("freezing")   
elif temp >= 0 and temp < 10:  # Simplified: 0 to 9
    print("cold")
elif temp >= 10 and temp < 20:  # 10 to 19
    print("moderate")
elif temp >= 20 and temp < 30:  # 20 to 29
    print("warm")
else:  # 30 and above
    print("hot") 