print("Hello there")
print("What is your name?")
answer = input()
print("Hello {}".format(answer))
print("Want to play a game?")
game = input()
if (game == "yes"):
    print("What should we play?")
    print("World of Warcraft or Overwatch")
    games = input()
    if (games == "World of Warcraft"):
        print("Good Choice")
    elif (games == "Overwatch"):
            print("Let's Go")
elif (game == "no"):
    print("Should we watch something?")
    video = input ()
    if ( video == "yes" ):
        print("What should we watch?")
        print("Netflix or Youtube")
        videos = input()
        if ( videos == "netflix" ):
            print("Cool")
        elif ( videos == "youtube" ):
            print("Ready to watch")
    elif ( video == "no" ):
        print("Should we find something to eat?")
