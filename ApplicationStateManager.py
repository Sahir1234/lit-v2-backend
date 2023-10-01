from common import IdManager
from errors import ClientError
from errors import StaleStateError
from lobby_manager import LobbyManager
from game_manager import GameManager

# Methods in this class are the ones that should be exposed by the API
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

    def get_lobby_state(self, id: str):
        if self.game_manager.is_game_id_active(id):
            # the lobby has been opened to a game, so need to update to the game page
            raise StaleStateError("Lobby \"" + id + "\" has started a game already!")
        else:
            return self.lobby_manager.get_lobby_state(id)
    

    def start_game(self, id: str):
        if self.lobby_manager.can_start_game(id):
            lobby = self.lobby_manager.close_lobby(id)
            self.game_manager.open_new_game(id, lobby)
        else:
            raise ClientError("Cannot start the game! Teams are uneven or there are not enough players!")

    # ask for a card
    # declare a set
    # get state (should be different per player)

    # LATER WE WILL ADD THE END OF GAME FUNCTIONALITY