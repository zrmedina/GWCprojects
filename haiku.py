from random import *

three = ["I like pie", "Friends are fun", "Food is great"]
five = ["I eat everyday", "We play games all night", "Chocolate is the best"]

responds = input("Want to hear a haiku?(y/n): ")

while responds != "n":
    if responds == "y":
        x = randint(0,len(three)-1)
        y = randint(0,len(five)-1)
        print(three[x])
        print(five[y])
        print(three[x])
    else:
        print("{} is a invalid responds".format(responds))
    responds = input("Want to hear a haiku?(y/n): ")
