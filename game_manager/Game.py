from lobby_manager import Lobby

class Game:

    def __init__(self, lobby: Lobby):
        self.red_team = lobby.get_read_team()
        self.blue_team = lobby.get_blue_team()

        self.curr_turn = lobby.get_admin()

        # initialize the cards and give admin the first turn
        # Player objets have no knowledge of what team they are on

        
        pass
        