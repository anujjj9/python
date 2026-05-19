import random 
import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

length = int(input("Enter the length of the password: "))
password = ""
characters = string.ascii_letters + string.digits + string.punctuation
if length < 8:
    print("Password should be at least 8 characters long.")
else:
    password = random.choice(uppercase)
    password = password + random.choice(lowercase)
    password = password + random.choice(digits)
    password = password + random.choice(symbols)
    for i in range(length-4):
        password += random.choice(characters)



    password = list(password)
    random.shuffle(password)
    password = ''.join(password)

    print("Generated password:", password)
