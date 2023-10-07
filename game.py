import random as ran
import time as tm




#users choice
user = input("Rock, Paper, or Scissor?")
user_option = user

# countdown
print("-")
print("Rock")
tm.sleep(2)
print("paper")
tm.sleep(2)
print("scissor")
tm.sleep(2)
print("Shoot!")

tm.sleep(3)

#computer choice 
choices = ["Rock","Paper", "Scissor"]
r = ran.choice(choices)
print("Computer:",r)
print("User:", user)

if user.lower == r.lower:
        print("TIE!")
    
elif(
    (user.lower == "rock" and r.lower == "scissor") or
    (user.lower == "paper" and r.lower == "rock") or
    (user.lower == "scissor" and r.lower == "paper")
    ):
        print("You win")
else:
        print("Computer Wins!")
        





