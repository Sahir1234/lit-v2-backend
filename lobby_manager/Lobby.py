from common import Player

class Lobby:

    MAX_PLAYERS: int = 12

    def __init__(self):
        # maps from name (str) to Player
        self.red_team = {}
        self.blue_team = {}
        
        self.admin = None


    def add_player(self, player: Player):
        player_name = player.get_name()
        self.validate_player_can_be_added(player_name)

        if len(self.red_team.keys()) <= len(self.blue_team.keys()):
            self.red_team[player_name] = player
        else:
            self.blue_team[player_name] = player
            
        if self.admin is None:
            # no admin set yet so make the first player admin
            self.admin = player_name

    
    def validate_player_can_be_added(self, player_name: str):
        if player_name is None or player_name == "":
            raise RuntimeError("Player name cannot be empty!")
        if self.is_lobby_full():
            raise RuntimeError("This lobby is full!")
        if player_name in self.red_team.keys() or player_name in self.blue_team.keys():
            raise RuntimeError("The name \"" + player_name + "\" is already taken!")
        

    def switch_player_team(self, player_name: str):
        if player_name in self.red_team.keys():
            player = self.red_team[player_name]
            del self.red_team[player_name]
            self.blue_team[player_name] = player
        elif player_name in self.blue_team.keys():
            player = self.blue_team[player_name]
            del self.blue_team[player_name]
            self.red_team[player_name] = player
        else:
            raise RuntimeError("Player \"" + player_name + "\" is not in this lobby!")


    def remove_player(self, player_name):
        if player_name in self.red_team.keys():
            del self.red_team[player_name]
        elif player_name in self.blue_team.keys():
            del self.blue_team[player_name]
        else:
            raise RuntimeError("Player \"" + player_name + "\" is not in this lobby!")

        if player_name == self.admin:
            self.set_new_admin()
    

    def set_new_admin(self):
        if not self.is_lobby_empty():
            all_players = self.get_all_players()
            self.admin = all_players[0]
        else:
            self.admin = None

    
    def is_lobby_empty(self):
        return len(self.get_all_players()) == 0
    

    def is_lobby_full(self) -> bool:
        return len(self.get_all_players()) >= Lobby.MAX_PLAYERS
    

    def get_all_players(self):
        return list(self.red_team.keys()) + list(self.blue_team.keys())


    def get_state(self) -> dict:
        state = {}
        state['red_team'] = self.red_team.keys()
        state['blue_team'] = self.blue_team.keys()
        state['admin'] = self.admin
        return state