import requests


response = requests.get("https://names.drycodes.com/1?combine=2&nameOptions=boy_names")
names = response.json()

def generateName():
    for i in names:
        res = i.split('_')
        return res

def generateFirstName():
    for i in names:
        res = i.split('_')[0]
        return res

def generateLastName():
    for i in names:
        res = i.split('_')[1]
        return res
