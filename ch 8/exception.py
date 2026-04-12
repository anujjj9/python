#a = int(input("Enter a number: "))
b = (input("Enter  number: "))
try:
#    print(10/a)
    print(100/b)
except Exception as err:
    print(f"the is error of {err}") #err is the variable which is used to print the error
else: print("no error")
finally: print("this will always execute")

print("divison done")
