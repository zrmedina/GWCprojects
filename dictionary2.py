dictionary = {"Zoe":17,"Alisha":49,"Logan":14,"Nick":46}
sum = 0
for names in dictionary:
    sum += dictionary[names]

average = sum / len(dictionary)
print("The average of the ages is: ")
print(average)
