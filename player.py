import json
from roller import DiceRoller

class Player:

    # this is a python constructor
    def __init__(self, playerDict):

        # self is a reference to the current instance of the class, used to store any member variables, etc.
        self.data = playerDict

    def get(self, key):
        return self.data[key]

    def __role_attribute(self, attribute_name):
        return DiceRoller.roll_successes(self.data["attributes"][attribute_name])

    def __roll_skill(self, skill_name: str):

        for skill in self.data["skills"]:
            if skill["name"] == skill_name:

                # add the attribute dices to the skill value and role for successes
                n_dice = self.data["attributes"][skill["attribute"]] + skill["value"]

                # if they have less than 1 die, they roll one die
                if n_dice <= 0:
                    n_dice = 1

                return DiceRoller.roll_successes(n_dice, dice_type="white")

        return 0 # automatic zero if you don't have the right skill

    def __roll_spell(self, spell_name: str):
        for spell in self.data["spells"]:
            if spell["name"] == spell_name:
                success_roll = self.__roll_skill(spell["type"])
                difficulty_roll = DiceRoller.roll_successes(spell["difficulty"], dice_type='black')

                return success_roll-difficulty_roll

    def handle_query(self, player_query: str):
        """
        Handles a query to the player by the discord bot
        :param player_query: the discord query with the name of the player removed
        :return: the result of the query
        """

        query_list = player_query.split('/')
        query_type = query_list[0]

        print(query_type)

        #check query type (i.e. first thing in the list) and act accordingly)

        if query_type == 'skill':
            skill_name = query_list[1]
            return self.__roll_skill(skill_name)

        if query_type == 'spell':
            spell_name = query_list[1]
            return self.__roll_spell(spell_name)


'''

# load the test character
charData = load_json_object('player1data.json')

# print full dictionary
print("This prints out the full dictionary");
print(charData)

# print the name of the characters 1st spell
#print("print the name of the characters 1st spell");
#print(charData['spells'][0]['name'])

# if you wanted to put multiple characters into the same file you could do this:
#print("if you wanted to put multiple characters into the same file you could do this:");
#playersData = load_json_object('multiple_player_data.json')

# this will print out an array of player dictionary objects
#print("Array: ")
#print(playersData)

# now we could loop over the dictionary objects and create player objects
#print("");
print("now we could loop over the dictionary objects and create player objects");
players = []
print("Create individual player objects: ")
for playerData in playersData:
    print(playerData)
    players.append(Player(playerData))
    
'''
"""
print("test number 1: ")
for thing in playersData:
    print(thing);


print("test number 2: ")
for players in players:
    print(playerData['speed'])
    #trying to get all speeds. got 1 speed 3 times


print("test number 3: ")
#this is will get us the right speeds with names
for playerData in playersData:
    print(playerData['name']+" "+str(playerData['speed']))

print(" ");
print("test number 4: ");
#this will give us data only if the name matches a preset variable
holder = "Neenerener 1";
for playerData in playersData:
    if(holder==playerData['name']):
        print(playerData['name']+" "+str(playerData['speed']))

""" 
print(" ");
print("test number 5: ");


'''def look_through_json(string):
    #take in input, parse it and throw out all the things
    holder=string;
    #holder = 'Neenerener/perception/0'
    print(holder);
    counter_name = 0;
    player_name = ""
    #this gets the charecter name
    for l in holder:
        print(l);
        print(counter_name);
        if l == '/':
            player_name = holder[:counter_name];
            print(player_name);
            break;
        else:
            counter_name=counter_name+1
            
    print(holder);

    #this gets the charecter skill
    player_skill = ""
    counter_skill=counter_name+1;
    for l in holder[counter_name+1:]:
        print(l);
        print(counter_skill);
        if l == '/':
            player_skill = holder[counter_name+1:counter_skill];
            print(player_skill);
            break;
        else:
            counter_skill=counter_skill+1
            
    #this gets the black dice number
    player_black = 0
    counter_black=counter_skill+1;
    for l in holder[counter_skill+1:]:
        print(l);
        print(counter_black);
        if l == '/':
            player_black = int(holder[counter_name+1:counter_black]);
            print(player_black);
            break;
        else:
            counter_black=counter_black+1
    print("The name is :"+player_name+"\n the skill is: "+player_skill+"\n The black dice number is: "+str(player_black))

    #now it will look up using the name and skill, printing out the value


    for playerData in playersData:
        if(player_name==playerData['name']):
            print("the skill value is: "+str(playerData[player_skill]))
            return playerData[player_skill];



look_through_json('Neenerener/perception/0');'''





