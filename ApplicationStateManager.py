import random
import string
from lobby_manager.LobbyManager import LobbyManager
from game_manager.GameManager import GameManager

class ApplicationStateManager:

    def __init__(self):
        self.lobby_manager = LobbyManager()
        self.game_manager = GameManager()
        self.active_ids = set()


    def generate_new_id(self):
        id = self.id_generator()
        while id in self.active_ids:
            id = self.id_generator
        return id
    
    def id_generator(self):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.SystemRandom().choice(chars) for _ in range(8))


    def open_new_lobby(self):
        new_id = self.generate_new_id()
        self.lobby_manager.open_new_lobby(new_id)
        self.active_ids.add(new_id)
        return new_id
    
    def add_player_to_lobby(self, player_name: str, id: str):
        self.lobby_manager.add_player_to_lobby(player_name, id)

    def swith_player_team_in_lobby(self, player_name: str, id: str):
        self.lobby_manager.switch_player_team_in_lobby(player_name, id)

    def remove_player_from_lobby(self, player_name: str, id: str):
        self.lobby_manager.remove_player_from_lobby(player_name, id)
        if not self.lobby_manager.is_lobby_active(id):
            # if the lobby closed due to no players, remove the id
            self.active_ids.remove(id)
    

     
