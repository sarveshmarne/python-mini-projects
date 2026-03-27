import random

option = ["Paper","Rock","Scissor"]

while True:
    
    computer = random.choice(option)
    user = str(input("Enter Rock, Paper, Scissor (or Quit to stop) :")).capitalize()
    
    if user == "Quit":
        print("Thank You for playing.")
        break
    
    if user not in option:
        print("Pick from the options given.")
        
    print(f"Computer choose : {computer}")    
    
    if computer == user:
        print("Its a Draw.")
    elif (user == "Paper" and computer == "Rock") or (user == "Rock" and computer == "Scissor") or (user == "Scissor" and computer == "Paper"):
        print("You Win") 
    else:
        print("You Lose")      
