import random

option = ["Stone", "Paper", "Scissor"]
computer = random.choice(option)
user = str(input("Enter : "))

if computer == user:
    print("You Win !!!")
else:
    print("You Lose.")    