from errors import ClientError
from errors import ServerError
from Player import Player

class Team:

    def __init__(self):
        # Player name -> Player object
        self.players_on_team = {}


    def add_player(self, player: Player):
        player_name = player.get_name()
        self.validate_player_can_be_added(player_name)
        self.players_on_team[player_name] = player


    def validate_player_can_be_added(self, player_name: str):
        if player_name is None or player_name == "":
            raise ClientError("Player name cannot be empty!")
        if player_name in self.players_on_team.keys():
            raise ClientError("The name \"" + player_name + "\" is already taken!")
        
    
    def has_player(self, player_name: str) -> bool:
        return player_name in self.players_on_team.keys()

    
    def remove_player(self, player_name: str) -> Player:
        if not player_name in self.players_on_team:
            # we should not be reaching here at all
            raise ServerError("Player \"" + player_name + "\" is not on this team!")
        player = self.players_on_team[player_name]
        del self.players_on_team[player_name]
        return player
    

    def get_players_on_team(self) -> list:
        return list(self.players_on_team.keys())


    def get_size_of_team(self) -> int:
        return len(self.players_on_team.keys())
