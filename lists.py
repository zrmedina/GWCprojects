from random import *

main = ["Steak", "Burgers", "Pizza"]
side = ["Fries", "Salad", "Soup"]
dessert = ["Icecream", "Cake", "Pie"]

x = randint(0, len(main)-1)
y = randint(0, len(side)-1)
z = randint(0, len(dessert)-1)
responds = input("Would you like a suggestion? (y/n): ")

while responds != "n":
    if responds == "y":
        x = randint(0, len(main)-1)
        y = randint(0, len(side)-1)
        z = randint(0, len(dessert)-1)
        print(main[x])
        print(side[y])
        print(dessert[z])
    else:
        print("Try Again")
    responds = input("Would you like a suggestion? (y/n): ")
