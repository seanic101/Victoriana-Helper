import json
from player import Player

class Game:

    @classmethod
    def __load_json_object(cls, filename):
        # open the file
        f = open(filename)

        # decode the json into a dictionary object
        return json.load(f)

    def __init__(self, player_data_file: str):
        players_data = self.__load_json_object(player_data_file)
        self.players = []

        # load in all players
        for player_data in players_data:
            self.players.append(Player(player_data))

    def __get_player_by_name(self, name: str):
        for player in self.players:
            if player.get("name") == name:
                return player

    def handle_bot_query(self, query: str):

        split_query = query.split('/', 1)
        player_name = split_query[0]
        if(query==split_query[0]):
            print("no length to query")
            return None;
        

        # find the player that the query was for
        player = self.__get_player_by_name(player_name)
        player_query = split_query[1]

        # pass the rest of the query to the player object
        return player.handle_query(player_query)
