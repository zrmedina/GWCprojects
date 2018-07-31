import json

file = open("tweets.json", "r")
data = json.load(file)

for d in data:
    #for info_cat, info in d.items():
    print(d["retweet_count"])
    break
