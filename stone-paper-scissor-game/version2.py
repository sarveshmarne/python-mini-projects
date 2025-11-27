import random

option = ["Paper", "Scissor", "Rock"]
computer = random.choice(option)

while True:
    user = str(input("Enter :"))
    
    if computer == user:
        print("You Win !!!")
    else:
        print("You Lose.")   