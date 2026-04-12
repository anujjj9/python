a = str(input("enter name"))
b = ""
#print(a[::-1])
for i in range(len(a)-1,-1,-1):
    b = b + (a[i])
if a == b:
    print("palindrome")
else:
    print("not palindrome")