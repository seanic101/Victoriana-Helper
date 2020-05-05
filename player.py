import json

class Player:

    # this is a python constructor
    def __init__(self, playerDict):

        # self is a reference to the current instance of the class, used to store any member variables, etc.
        self.data = playerDict

def load_json_object(filename):
    # open the file
    f = open(filename)

    # decode the json into a dictionary object
    return json.load(f)

# load the test character
charData = load_json_object('player1data.json')

# print full dictionary
print(charData)

# print the name of the characters 1st spell
print(charData['spells'][0]['name'])

# if you wanted to put multiple characters into the same file you could do this:
playersData = load_json_object('multiple_player_data.json')

# this will print out an array of player dictionary objects
print("Array: ")
print(playersData)

# now we could loop over the dictionary objects and create player objects
players = []
print("Create individual player objects: ")
for playerData in playersData:
    print(playerData)
    players.append(Player(playerData))