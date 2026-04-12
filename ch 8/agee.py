a = int(input("Enter a number: "))
try:
    if a<0:
        raise Exception("Negative number not allowed") #this is how we can raise an exception
    else:
        print(f"the number is {a}")
except Exception as err:
    print(f"Error: {err}")
except Exception as e:
    print(f"Error: {e}")
print("number is valid")