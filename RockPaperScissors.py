import os
os.system('clear')

user = str(raw_input("Pick one!" + "\n" + "Rock" + "\n" + "Paper" + "\n" + "Scissors" + "\n"))
user = user.lower()

choices = ["rock", "paper", "scissors"]

import random
comp = random.choice(choices)

if user == "rock" and comp == "scissors" or user == "paper" and comp == "rock" or user == "scissors" and comp == "paper" :
    os.system('clear')
    print "Player 2 picked %s! You won!" %(comp)

elif user == "rock" and comp == "paper" or user == "paper" and comp == "scissors" or user == "scissors" and comp == "rock" :
    os.system('clear')
    print "Player 2 picked %s! You lost!" %(comp)

elif user == "rock" and comp == "rock" or user == "paper" and comp == "paper" or user == "scissors" and comp == "scissors" :
    os.system('clear')
    print "Player 2 picked %s! Even game!" %(comp)
    
else :
    print "Oops! something went wrong."
