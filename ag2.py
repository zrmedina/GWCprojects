answer = "none"
while (answer != "Beach" or "Downtown" or "Clothing Store") :
    answer = input("Beach, Downtown, or Clothing Store: ")
    if (answer == "Beach") :
        print("You: Let's go hang out at the beach!")
        print("You: Wow it's such a nice day today.")
        print("Friend: Yeah I am so excited to be at the beach.")
        print("You: Hey, I think we should go in the water.")
        print("Friend: Well, I kind of wanted to tan")
        answer2 = input("You: Should we go in the WATER or stay and TAN?: ")
        print("\n")
        while (answer2 != "WATER" or "TAN") :
            if (answer2 == "WATER") :
                print("You: Yay! Let's go play in the waves!")
                print("As you head for the water a shark appears and chases you on land")
                print("You: Run!")
                continue
            elif (answer2 == "TAN") :
                print("You: Aww okay. We can stay here and tan then.")
                print("You guys spend the rest of the day on the sand")
                print("Friend: Wow my tan is so amazing!")
                print("You: Mine too!")
                continue
