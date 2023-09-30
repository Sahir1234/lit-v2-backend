import random
from common import Player
from common import Team
from errors import ClientError
from errors import ServerError

class Lobby:

    MIN_PLAYERS: int = 4
    MAX_PLAYERS: int = 12

    def __init__(self):
        # maps from name (str) to Player
        self.red_team = Team()
        self.blue_team = Team()
        self.admin = None


    def get_read_team(self) -> Team:
        return self.red_team
    

    def get_blue_team(self) -> Team:
        return self.blue_team
    

    def get_admin(self) -> str:
        return self.admin


    def add_player(self, player: Player):
        player_name = player.get_name()
        if self.is_lobby_full():
            raise ClientError("This lobby is full!")

        if len(self.red_team.keys()) <= len(self.blue_team.keys()):
            self.red_team.add_player(player)
        else:
            self.blue_team.add_player(player)
            
        if self.admin is None:
            # no admin set yet so make the first player admin
            self.admin = player_name
        

    def switch_player_team(self, player_name: str):
        if self.red_team.has_player(player_name):
            player = self.red_team.remove_player(player_name)
            self.blue_team.add_player(player)
        elif self.blue_team.has_player(player_name):
            player = self.blue_team.remove_player(player_name)
            self.red_team.add_player(player)
        else:
            # We should not be reaching here at all
            raise ServerError("Player \"" + player_name + "\" is not in this lobby!")
        

    def randomize_teams(self):
        all_player_names = self.get_all_players()
        all_players = {}

        for player_name in all_player_names:
            player = self.remove_player(player_name)
            all_players[player_name] = player

        random.shuffle(all_player_names)
        for player_name in all_player_names:
            self.add_player(all_players[player_name])


    def remove_player(self, player_name) -> Player:
        player_removed = None
        if self.red_team.has_player(player_name):
            player_removed = self.red_team.remove_player(player_name)
        elif self.blue_team.has_player(player_name):
            player_removed = self.blue_team.remove_player(player_name)
        else:
            # We should not be reahing here at all
            raise ServerError("Player \"" + player_name + "\" is not in this lobby!")

        if player_name == self.admin:
            self.set_new_admin()

        return player_removed
    

    def set_new_admin(self):
        if not self.is_lobby_empty():
            all_players = self.get_all_players()
            self.admin = all_players[0]
        else:
            self.admin = None
    

    def can_start_game(self) -> bool:
        return self.are_teams_even() and self.does_lobby_have_enough_players()
    

    def is_lobby_empty(self) -> bool:
        total_players_count = self.red_team.get_size_of_team() + self.blue_team.get_size_of_team()
        return total_players_count == 0
    

    def is_lobby_full(self) -> bool:
        total_players_count = self.red_team.get_size_of_team() + self.blue_team.get_size_of_team()
        return total_players_count >= Lobby.MAX_PLAYERS


    def does_lobby_have_enough_players(self) -> bool:
        total_players_count = self.red_team.get_size_of_team() + self.blue_team.get_size_of_team()
        return total_players_count >= Lobby.MIN_PLAYERS


    def are_teams_even(self) -> bool:
        return self.red_team.get_size_of_team() == self.blue_team.get_size_of_team()
    

    def get_all_players(self):
        return list(self.red_team.get_players_on_team()) + list(self.blue_team.get_players_on_team())


    def get_state(self) -> dict:
        state = {}
        state['red_team'] = self.red_team.get_players_on_team()
        state['blue_team'] = self.blue_team.get_players_on_team()
        state['admin'] = self.admin
        return state
