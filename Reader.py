import json

def load_json_object(filename):
    # open the file
    f = open(filename)

    # decode the json into a dictionary object
    return json.load(f)

# load the test character
charData = load_json_object('testchar.json')

# print full dictionary
print(charData)

# print the name of the characters 1st spell
print(charData['spells'][0]['name'])

