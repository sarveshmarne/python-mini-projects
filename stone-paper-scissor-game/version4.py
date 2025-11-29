import random

option = ["Paper", "Rock", "Scissor"]

user_score = 0
computer_score = 0

round = random.choice([3, 5, 7])

print(f"The games winner will be decided in {round} rounds.")

if round == 3:
    win_score = 2
elif round == 5:
    win_score = 3
else:
    win_score =  4       

while user_score < win_score and computer_score < win_score:
    
    computer = random.choice(option)
    user = str(input("Enter Rock, Paper, Scissor (or Quit to end) : ")).capitalize()
    
    if user == "Quit":
        print(f"Thank for Playing")
        break
        
    if user not in option:
        print(f"Select the given options.")
        continue
        
    if user==computer:
        print("Its a Tie")
    elif (user == "Paper" and computer == "Rock") or (user == "Scissor" and computer == "Paper") or (user == "Rock" and computer == "Scissor"):
        print(f"You Won")
        user_score = user_score + 1
    else:
        print(f"Computer Won") 
        computer_score = computer_score + 1
          
if user_score >= win_score:
    print("Congratulations You Won !!!")
elif computer_score >= win_score:
    print(f"Bad Luck, Computer Won.")                   