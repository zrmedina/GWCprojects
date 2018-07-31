import json
import os
questions = {"Name" : "What is your name?: ",
"DoB" : "What is your date of birth? (MM/DD/YYYY): ",
"Age" : "What is your age?: ",
"Home" : "Where do you call home? (City, State, Country): ",
"Hours_On_Phone" : "How many hours per week do you spend on the phone?: "}
responses = []
def survey():
    response = {}
    for data, question in questions.items():
        answer = input(question)
        response[data] = answer
    responses.append(response)
while True:
    print("\n")
    print("What would you like to do? \n Start to start survey \n Clear to clear data \n Data to check data \n Save to save data to json file")
    choice = input()
    if choice == "Start":
        print("\n")
        survey()
    if choice == "Clear":
        responses = []
        continue
    if choice == "Data":
        print("\n")
        print(responses)
        continue
    if choice == "Save":
        file = open("survey2.json", "r+")
        old_data = json.load(file)
        old_data.extend(responses)
        file.write(json.data(old_data))
        file.close()
