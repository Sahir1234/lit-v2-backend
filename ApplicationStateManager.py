from common import IdManager
from lobby_manager import LobbyManager
from game_manager import GameManager

class ApplicationStateManager:

    def __init__(self):
        self.id_manager = IdManager()
        self.lobby_manager = LobbyManager()
        self.game_manager = GameManager()


    def open_new_lobby(self):
        new_id = self.generate_new_id()
        self.lobby_manager.open_new_lobby(new_id)
        self.id_manager.add_new_active_id(new_id)
        return new_id
    
    def add_player_to_lobby(self, player_name: str, id: str):
        self.lobby_manager.add_player_to_lobby(player_name, id)

    def swith_player_team_in_lobby(self, player_name: str, id: str):
        self.lobby_manager.switch_player_team_in_lobby(player_name, id)

    def randomize_teams_in_lobby(self, id: str):
        self.lobby_manager.randomize_teams(id)

    def remove_player_from_lobby(self, player_name: str, id: str):
        self.lobby_manager.remove_player_from_lobby(player_name, id)
        if not self.lobby_manager.is_lobby_active(id):
            # if the lobby closed due to no players, remove the id
            self.id_manager.remove_active_id(id)
    

     
