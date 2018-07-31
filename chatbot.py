# --- Define your funtions below! ---
from random import *

def intro():
    print("Welcome to ChatBot!")

def greeting():
    yourname = input("\nWhat is your name?:  ")
    print("Nice to meet you {}".format(yourname))

def rps():
    you = input("rock, paper, or scissors? " )
    hand = ["rock", "paper", "scissors"]
    choice = randint(0,len(hand)-1)
    print(hand[choice])
    if you == "rock" and hand[choice] == hand[1]:
        print("I win!")
    elif you == "paper" and hand[choice] == hand[2]:
        print("I win!")
    elif you == "scissors" and hand[choice] == hand[0]:
        print("I win!")
    elif you == hand[choice]:
        print("It's a tie")
    else:
        print("You win!")
def poems():
    list = ["Now close the windows and hush all the fields:\nIf the trees must, let them silently toss;\nNo bird is singing now, and if there is,\nBe it my loss.",
            "The way a crow\nShook down on me\nThe dust of snow\nFrom a hemlock tree\nHas given my heart\nA change of mood\nAnd saved some part\nOf a day I had rued."]

    take = randint(0,len(list)-1)
    print(list[take])
def is_valid(responds, all_valid):
    valid = ["yes", "y", "Yes", "YES"]
    if responds in all_valid:
        return True
    else:
        return False
def gtn2():
    number = randint(0,20)
    tries = 0
    print("What number am I thinking of from 0-20?")
    yours = int(input("Guess a Number: "))

    for tries in range(2) :
        if yours < number :
            yours = int(input("Guess Higher: "))
        elif yours > number :
            yours = int(input("Guess Lower: "))
        else :
            break

    print("The number was {}".format(number))
    print("Thanks for playing")

def end():
    valid = ["yes", "y", "Yes", "YES"]
    print("Thanks for playing!")
    repeat = input("Play again? (y/n): ")
    if is_valid(repeat, valid):
        start()
    elif repeat == "n":
        print("Goodbye {}".format(yourname))
def start():
    if __name__ == "__main__":
        main()

# --- Put your main program below! ---
def main():
    yourname = ""
    valid = ["yes", "y", "Yes", "YES"]
    intro()
    while True:
        answer = input("\nWant to chat? (y/n): ")
        if is_valid(answer, valid):
            yourname = input("\nWhat is your name?:  ")
            print("Nice to meet you {}".format(yourname))
            break
        else:
            print("please type one of these:")
            for vi in valid:
                print(vi)
    while True:
        game = input("\nWant to play rock-paper-scissors? (y/n): ")
        if is_valid(game, valid):
            rps()
            print("Good game {}".format(yourname))
        elif game == "n":
            break
    while True:
        poem = input("\nWant to hear a poem? (y/n): ")
        if is_valid(poem, valid):
            poems()
        elif poem == "n":
            break
    while True:
        gtn = input("\nWant to guess what number I am thinking of? (y/n): ")
        if is_valid(gtn, valid):
            gtn2()
        elif gtn == "n":
            break
    end()

#Don't touch! Setup code that runs your main() function
if __name__ == "__main__":
    main()
