n = int(input("enter num:"))
sum_even = 0
sum_odd = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"sum of even num is {sum_even}")
print(f"sum of odd num is {sum_odd}")