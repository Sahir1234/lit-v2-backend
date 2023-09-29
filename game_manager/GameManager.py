import Game
import uuid
from uuid import UUID

class GameManager:

    def __init__(self):
        # ID (str) -> Game
        self.games: dict = {}

    def open_new_game
