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
