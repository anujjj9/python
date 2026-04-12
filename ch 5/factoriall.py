def fact(n):
    """
    Calculate the factorial of a given number.
    
    Args:
        n (int): The number for which to calculate the factorial.
    
    Returns:
        None (prints the result directly)
    """
    fact = 1
    # Multiply all numbers from 1 to n
    for i in range(1, n + 1):
        fact = fact * i
    
    print(f"factorial is {fact}")

# Get user input and calculate factorial
num = int(input("enter number: "))
fact(num)
