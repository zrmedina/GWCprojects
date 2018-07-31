import json
def analysis():
    file = open("survey2.json", "r")
    convert = json.load(file)
    sum = 0
    for response in convert:
        sum += int(response["Age"])
    average = sum / len(convert)
    print("Average of participants ages ")
    print(average)
    print()
    state_count = {}
    for d in convert:
        state_count[d["Home"]] =  state_count.get(d["Home"], 0) + 1
    print("Home by percentage of participants")
    for state, count in state_count.items():
        print("{}: {}%".format(state, 100 * count/ len(convert)))
    print()
    print("Youngest and oldest participants")
    age_sort = sorted(convert, key=lambda k: int(k['Age']))
    print("Youngest: {}, age {}".format(age_sort[0]["Name"], age_sort[0]["Age"]))
    print("Oldest: {}, age {}".format(age_sort[-1]["Name"], age_sort[-1]["Age"]))
analysis()
