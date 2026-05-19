import random

print("Let's start the game!!!!!")

secret_number = random.randint(1,100)
attempts = 0

while True:

    guess = int(input("Enter a number: "))
    attempts += 1

    if guess < secret_number:
        print("Go higher!")

    elif guess > secret_number:
        print("Go lower!")

    else:
        print("Correct!!")
        print("Attempts:", attempts)
        break