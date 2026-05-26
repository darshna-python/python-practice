import random

secret = random.randint(1,10)

guess = int(input("Guess a number between 1 to 10: "))
if guess == secret:
    print("Correct! you Won ")
else:
    print("Wrong!")
    print("The number was",secret)
