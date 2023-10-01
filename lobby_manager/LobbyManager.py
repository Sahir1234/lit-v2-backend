from Lobby import Lobby
from common import Player
from errors import ClientError

class LobbyManager:

    def __init__(self):
        # ID (str) -> Lobby
        self.lobbies: dict = {}


    def open_new_lobby(self, id: str) -> str:
        if self.is_lobby_id_active(id):
            raise ClientError("Lobby with id " + id + " already exists!")
        self.lobbies[id] = Lobby()
        
    
    def get_lobby(self, id: str) -> Lobby:
        if self.is_lobby_id_active(id):
            return self.lobbies[id]
        else:
            raise ClientError("Lobby with id " + id + " does not exist!")
        

    def is_lobby_id_active(self, id: str) -> bool:
        return id in self.lobbies.keys()


    def add_player_to_lobby(self, player_name: str, id: str):
        lobby = self.get_lobby(id)
        lobby.add_player(Player(player_name))


    def switch_player_team_in_lobby(self, player_name: str, id: str):
        lobby = self.get_lobby(id)
        lobby.switch_player_team(player_name)


    def randomize_teams(self, id: str):
        lobby = self.get_lobby(id)
        lobby.randomize_teams()
        

    def remove_player_from_lobby(self, player_name: str, id: str):
        lobby = self.get_lobby(id)
        lobby.remove_player(player_name)
        self.close_lobby(id)


    def close_lobby(self, id: str) -> Lobby:
        lobby = self.get_lobby(id)
        del self.lobbies[id]
        return lobby
    

    def can_start_game(self, id: str) -> bool:
        lobby = self.get_lobby(id)
        return lobby.can_start_game()
    
    
    def get_lobby_state(self, id: str) -> dict:
        return self.get_lobby(id).get_state()
