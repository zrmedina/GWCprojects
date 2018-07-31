
import json

from textblob import TextBlob

import matplotlib.pyplot as plt


tweetFile = open("tweets.json", "r")

tweetData = json.load(tweetFile)

polarity_values = []

for tweet in tweetData:
    tweet_text = tweet["text"]
    tb = TextBlob(tweet_text)
    print("{}: {}".format(tweet_text, tb.polarity))
    print()
    polarity_values.append(tb.polarity)

tweetFile.close()

#bins = [-1,-0.5,0,0.5,1]
plt.hist(polarity_values)
plt.title("Tweet Polarity")
plt.ylabel("Count of Tweets")
plt.xlabel("Polarity")
plt.show()
