
print("You: What should we do today?")
answer = input("Beach, Downtown, or Clothing Store: ")
print("\n")
if (answer == "Beach") :
    print("You: Let's go hang out at the beach!")
    print("You: Wow it's such a nice day today.")
    print("Friend: Yeah I am so excited to be at the beach.")
    print("You: Hey, I think we should go in the water.")
    print("Friend: Well, I kind of wanted to tan")
    answer2 = input("You: Should we go in the WATER or stay and TAN?: ")
    print("\n")
    if (answer2 == "WATER") :
        print("You: Yay! Let's go play in the waves!")
        print("As you head for the water a shark appears and chases you on land")
        print("You: Run!")
    elif (answer2 == "TAN") :
        print("You: Aww okay. We can stay here and tan then.")
        print("You guys spend the rest of the day on the sand")
        print("Friend: Wow my tan is so amazing!")
        print("You: Mine too!")
elif (answer == "Downtown") :
    print("You: There is a bunch to do downtown!")
    print("Wow, there's not a lot of people here today!")
    print("Friend: Yeah we have the city to ourselves.")
    print("You: I am hungry. Let's get some food.")
    print("Friend: But I wanted to go watch a movie.")
    answer3 = input("You: Should we get something to EAT or watch a MOVIE?: ")
    print("\n")
    if (answer3 == "EAT") :
        print("You: Good. I am starving")
        print("You: These cheesy-puffs are sooo good!")
        print("Friend: Yeah, my taco is delicious!")
    elif (answer3 == "MOVIE") :
        print("You: Fine. I'll just get food in the theater.")
        print("You: Check your phone for movie times.")
        print("Friend: Oh no, all the shows are sold out!")
        print("You: Oh well. Let's go get food then.")
        print("You: These cheesy-puffs are sooo good!")
        print("Friend: Yeah, my taco is delicious!")
elif (answer == "Clothing Store") :
    print("You: I need to get some new clothing!")
    print("You: Wow friend, I really like those glasses on you.")
    print("Friend: Thanks. I know I look good.")
    print("You: Wait, how are you going to pay for those?")
    print("Friend: No one is looking, I could just take them.")
    answer4 = input("You: Should we PAY for the glasses or STEAL them?: ")
    print("\n")
    if (answer4 == "PAY") :
        print("You: I will just lend you the money.")
        print("Friend: Fine. I'll go find a cashier.")
        print("You: Okay. I'll wait here.")
    elif (answer4 == "STEAL") :
        print("You: Fine. Let's hurry and get out of here.")
        print("Security: Hey! Where are you guys going with those glasses?!")
        print("Friend: Run!!!!")