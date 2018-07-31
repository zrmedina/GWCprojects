from random import *
import random
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

def gtn():
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

def word():
    words = ["hello", "complex","shelter","pinch","canvas","sin","fade","refused",
    "rain","adamant","face","venomous","mark","parched","possess","teeth",
    "building","love","gaudy","modern","ruthless","jumpy","remarkable",
    "colour","jeans"]
    for w in words:
        phrases = random.choice(words)
    return phrases
def text(phrase,guessed):
    display = ""
    for letter in phrase:
        if letter in guessed:
            display += letter
        elif letter == " ":
            display += "  "
        else:
            display += "_ "
    return display
def h_m():
    game_over = False
    phrase = word()
    guessed = []
    text2 = text(phrase,guessed)
    print(text2)
    while game_over != True:
        guess = input("Enter a letter: ")
        guessed.append(guess)
        text3 = text(phrase,guessed)
        print(text3)
        if "_ " in text3:
            game_over = False
        else:
            game_over = True
    print("You did it! The answer was {}".format(phrase))

def evenorodd():
    computer_value = random.randint(1,10)
    print("{}".format(computer_value))
    user_input = input("Is this number even or odd? ")
    if computer_value%2 == 0 and user_input == "even":
        print("Good job!")
    elif computer_value%2 != 0 and user_input == "odd":
        print("Good job!")
    else:
        print("Wrong.")

def madlib():
    import random
    noun_list = []
    verb_list = []
    for n in range(3):
        noun = input("Give me a noun: ")
        noun_list.append(noun)
    for v in range(3):
        verb = input("Give me a verb: ")
        verb_list.append(verb)
    story = """
        There once was a girl named Sally. She woke up at 6 am everyday and _ .
        One day she visited a __ and saw a bunch of animals. Sally decided to _ and
        then walk away. An hour later she visited her friends at the __ and they _
        for the rest of the day. In the end, she grabbed her __ and headed home.
        """
    story_list = story.split()
    new_story_list = []
    dict = {"__" : random.choice(noun_list), "_" : random.choice(verb_list) }

    for word in story_list:
        if word in dict:
            new_story_list.append(dict[word])
        elif word in dict:
            new_story_list.append(dict[word])
        else:
            new_story_list.append(word)

    print(" ".join(new_story_list))
