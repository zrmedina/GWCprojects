import gameplay
from random import *

available_games = ["Rock Paper Scissors", "Even or Odd", "Guess the Number", "Hangman", "Mad Libs"]

def start_game():
    print("Welcome to the GameHub!")
    print("Here is a list of available games:")
    for g in available_games:
        print(g)
def evaluate():
    a = input("What do you want to play?: ")
    if a == "Rock Paper Scissors":
        gameplay.rps()
    elif a == "Even or Odd":
        gameplay.evenorodd()
    elif a == "Guess the Number":
        gameplay.gtn()
    elif a == "Hangman":
        gameplay.h_m()
    elif a == "Mad Libs":
        gameplay.madlib()
    else:
        evaluate()
def go():
    start = True
    while start != False:
        start_game()
        evaluate()
        play_again = input("Do you wish to play again? (y/n): ")
        if play_again == "y":
            start = True
        else:
            start = False
if __name__ == "__main__":
    go()
