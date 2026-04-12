def prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1

    if count > 2:
        print("not a prime number")
    else:
        print("prime number")

num = int(input("enter number: "))
prime(num)