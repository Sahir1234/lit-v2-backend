from Game import Game
from errors import ServerError
from lobby_manager import Lobby

class GameManager:

    def __init__(self):
        # ID (str) -> Game
        self.games: dict = {}

    def open_new_game(self, id: str, lobby: Lobby):
        if self.is_game_id_active(id):
            raise ServerError("Game with id " + id + " already exists!")
        self.games[id] = Game(lobby)


    def get_game(self, id: str) -> Game:
        if self.is_game_id_active(id):
            return self.games[id]
        else:
            raise ServerError("Game with id " + id + " does not exist!")
        

    def is_game_id_active(self, id: str) -> bool:
        return id in self.games.keys()
    

    def close_game(self, id: str) -> Game:
        game = self.get_game(id)
        del self.games[id]
        return game
    

    def get_game_state(self, id: str) -> dict:
        return self.get_game(id).get_state()
    
