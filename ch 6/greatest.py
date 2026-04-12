a = [12, -47, 44, 444, 33, -77, -87, 6]
greatest = a[0]
for i in range(len(a)):
    if a[i] > greatest:
        greatest = a[i-1]
        index = i-1
print(f"greatest num is {greatest} and its index value is {index}")

