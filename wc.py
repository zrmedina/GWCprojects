import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

long_text = []
for tweet in tweetData:
    tweet_text = tweet["text"]
    long_text.append(tweet_text)
long = " ".join(long_text)

tb = TextBlob(long)
list_words = long.split()

diction = {}

for word in list_words:
    word = word.lower().rstrip().lstrip()
    if "http" in word:
        continue
    if word[0] == "#" or word[0] == "@":
        word = word [1: ]
    if len(word) < 4:
        continue
    if word[-1] in {",", "?", ".", ":", "/", "!", '"', "'"}:
        word = word[: -1]
    diction[word] = diction.get(word, 0) + 1

word_count = {}
for word, count in diction.items():
    if count < 2:
        continue
    else:
        word_count[word] = count
word_cloud = WordCloud().generate_from_frequencies(word_count)
plt.imshow(word_cloud, interpolation = 'bilinear')
plt.show()
