n = int(input("enter number"))
factor=0
for i in range(1,n+1):
    if n % i == 0:
        factor = factor + 1
if factor >3:
  print("prime")
else:
  print("not prime")
