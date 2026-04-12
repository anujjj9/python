def fibonacci(n):

    a = 0
    b = 1
    
    # Generate n Fibonacci numbers by adding previous two numbers
    for i in range(n):
        print(a, end=" ")
        c = a + b  # Next Fibonacci number
        a = b      # Shift values forward
        b = c

# Get number of terms from user and display Fibonacci sequence
num = int(input("Enter number of terms: "))
fibonacci(num)