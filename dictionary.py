dict = {'imo':'in my opinion',
        'lol': 'league of legend',
        'smh': 'shaking my head',
        'wow': 'world of warcraft',
        'gwcsip': 'girls who code summer immersion program',
        'wtf': 'what the fark',
        'w/e': 'whatever'}

def translate_shorthand(dictionary):
    for k, v in sorted(dictionary.items()):
        print(k, v)

translate_shorthand(dict)

story = """
Stacy was texting. She said lol noobs suck smh . imo wow is better. Are you going to gwcsip ?
"""
story_list = story.split()

new_story_list = []
for word in story_list:
    if word in dict.keys():
        new_story_list.append(dict[word])
    else:
        new_story_list.append(word)

print(" ".join(new_story_list))
