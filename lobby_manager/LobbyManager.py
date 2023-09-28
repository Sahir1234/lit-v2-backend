import Lobby
from common import Player

class LobbyManager:

    def __init__(self):
        # ID (str) -> Game
        self.lobbies: dict = {}


    def open_new_lobby(self, id: str) -> str:
        if id in self.lobbies.keys():
            raise RuntimeError("Lobby with id " + id + " already exists!")
        self.lobbies[id] = Lobby()
        

    def add_player_to_lobby(self, player_name: str, id: str):
        lobby = self.get_lobby(id)
        lobby.add_player(Player(player_name))


    def switch_player_team_in_lobby(self, player_name: str, id: str):
        lobby = self.get_lobby(id)
        lobby.switch_player_team(player_name)


    def remove_player_from_lobby(self, player_name: str, id: str):
        lobby = self.get_lobby(id)
        lobby.remove_player(player_name)
        if lobby.is_empty():
            del self.lobbies[id]


    def get_lobby(self, id: str) -> Lobby:
        if self.is_lobby_id_active(id):
            return self.lobbies[id]
        else:
            raise RuntimeError("Lobby with id " + id + " does not exist!")
        

    def is_lobby_id_active(self, id: str):
        return id in self.lobbies.keys()
