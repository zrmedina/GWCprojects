def letter_frequency(word):
    frequency = {}

    for char in word:
        if char in frequency.keys():
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1
    print(frequency)

letter_frequency("pen pineapple apple pen")
