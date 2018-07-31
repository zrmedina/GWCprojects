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

list_words = long.split()

positive = []
negative = []
neutral = []

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
    word_polarity = TextBlob(word).polarity
    if word_polarity < -0.25:
        negative.append(word)
    if word_polarity > 0.25:
        positive.append(word)
    else:
        neutral.append(word)

positive_count = {}
positive_count2 = {}
for word in positive:
    positive_count[word] = positive_count.get(word, 0) + 1
    for word, count in positive_count.items():
        if count < 2:
            continue
        else:
            positive_count2[word] = count

word_cloud = WordCloud().generate_from_frequencies(positive_count2)
plt.imshow(word_cloud, interpolation = 'bilinear')
plt.show()

neutral_count = {}
neutral_count2 = {}
for word in neutral:
    neutral_count[word] = neutral_count.get(word, 0) + 1
    for word, count in neutral_count.items():
        if count < 2:
            continue
        else:
            neutral_count2[word] = count

word_cloud = WordCloud().generate_from_frequencies(neutral_count2)
plt.imshow(word_cloud, interpolation = 'bilinear')
plt.show()

negative_count = {}
negative_count2 = {}
for word in negative:
    negative_count[word] = negative_count.get(word, 0) + 1
    for word, count in negative_count.items():
        if count < 2:
            continue
        else:
            negative_count2[word] = count

word_cloud = WordCloud().generate_from_frequencies(negative_count2)
plt.imshow(word_cloud, interpolation = 'bilinear')
plt.show()
