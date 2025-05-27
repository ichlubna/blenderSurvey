import json

survey = []
with open('a.json', 'r') as file:
    for line in file:
        survey.append(json.loads(line))

for s in survey:
    if "multi__kind_of_work__other" in s: 
        print(s["multi__kind_of_work__other"])
