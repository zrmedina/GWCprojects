import random
number = int(random.uniform(0,20))
tries = 0
print("What number am I thinking of from 0-20?")
answer = int(input("Guess a Number: "))

for tries in range(2) :
    if answer < number :
        answer = int(input("Guess Higher: "))
    elif answer > number :
        answer = int(input("Guess Lower: "))
    else :
        break

print("The number was {}".format(number))
print("Thanks for playing")
