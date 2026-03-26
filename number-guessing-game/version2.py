import random 

number = random.randint(1,100)

while True:
    user = int(input("Guess the number from 1-100 :"))
    
    if user == number:
        print("You Guessed the right number !!!")
        break
    elif user > number:
        print("Too high, Try again.", user)
    else:
        print("Too low, Try again.", user)  