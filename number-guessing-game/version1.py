import random 
user = int(input("Guess the number from 1-100 : "))
if user == random.randint(1,100):
    print("You Guessed it right !!!")
else:
    print("Try Again")  