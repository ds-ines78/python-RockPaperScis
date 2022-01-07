"""
Rock Paper Scissors game
"""

import random

round_count = 1
#user_wins = 0
#sys_wins = 0

def rps_game():
    print(f"Round {round_count}")
    
    #user's turn
    print("Rock, paper, or scissors?")
    user_throw = input()
    if user_throw in ("ROCK", "Rock", "rock", "R", "r", "PAPER", "Paper", "paper", "P", "p", "SCISSORS", "Scissors", "scissors", "S", "s"):
        print("You threw " + user_throw + ".")
    print("-------------------")

    #system's turn
    throw = ["rock", "paper", "scissors"]
    sys_throw = random.choice(throw)
    print("System threw " + sys_throw + ".")
    print("-------------------")

    user_wins = 0
    sys_wins = 0
    
    if user_throw in ("rock", "Rock", "ROCK", "R", "r"):
        if sys_throw == "rock":
            print("It's a draw.")
        elif sys_throw == "paper":
            print("System wins!")
            sys_wins = sys_wins + 1
        elif sys_throw == "scissors":
            print("You win!")
            user_wins = user_wins + 1
    elif user_throw in ("paper", "Paper", "PAPER", "P", "p"):
        if sys_throw == "paper":
            print("It's a draw.")
        elif sys_throw == "scissors":
            print("System wins!")
            sys_wins = sys_wins + 1
        elif sys_throw == "rock":
            print("You win!")
            user_wins = user_wins + 1
    elif user_throw in ("scissors", "Scissors", "SCISSORS", "S", "s"):
        if sys_throw == "scissors":
            print("It's a draw.")
        elif sys_throw == "rock":
            print("System wins!")
            sys_wins = sys_wins + 1
        elif sys_throw == "paper":
            print("You win!")
            user_wins = user_wins + 1

    print("-------------------")
    print(f"User : {user_wins}, System : {sys_wins}")

   
rps_game()

print(" ")
print(" ")

repeat_play = input("Restart? ")

while repeat_play in ("Y", "y", "yes", "Yes"):
    print("-------------------")
    print(" ")
    round_count = round_count + 1
    rps_game()

if repeat_play in ("N", "n", "no", "No"):
    print("Thanks for playing.")
    quit

round_count = round_count





        
