score = 0
print("Welcome to Quiz game")

answer = input("Q1. What is the capital of India? ")
if answer.lower() == "delhi":
    print("Correct!")
    score = score + 1

else:
    print("Wrong!")

answer = int(input("Q2. What is 2 + 2"))
if answer == 4:
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("Q3. what language are you learning?")
if answer.lower() == "python":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")
print("Your total score is:",score)

