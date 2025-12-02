import random

number = random.randint(1,100)
attempts = random.randint(1,10)
print(f"You will get {attempts} attempts.")

for i in range(attempts):
    user = float(input(f"Enter your guess:"))
   
    if user == number:
        print("You Guessed the right number !!!")
        break
    elif user > number:
        print("Too high, Try again.", user)
    else:
        print("Too low, Try again.", user) 
    
    if attempts - (i + 1) > 1:    
        print("Attempts left :", attempts - (i + 1))   
    elif attempts - (i + 1) == 1:
        print(f"Last attempt left.")    
    else:
        print(f"You are out of attempts. The number was {number}.")      