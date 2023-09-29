import Card
import Player

class Player:

    def __init__(self, name: str):
        self.name: str = name
        self.hand: list = []

    def get_name(self) -> str:
        return self.names
    
    def set_hand(self, hand: list):
        self.hand = hand
    
    def has_card(self, card: Card) -> bool:
        return card in self.hand

    def can_ask_player_for_this_card(self, player_to_ask: Player, card_to_ask: Card) -> bool:
        return (not self.team == player_to_ask.get_team()) and \
            (self.can_ask_for_this_card(card_to_ask))

    def can_ask_for_this_card(self, card_to_ask: Card) -> bool:
        return (not self.has_card(card_to_ask)) and \
            (self.has_card_in_set(card_to_ask.get_set()))

    def has_card_in_set(self, set_to_check: Card.Set) -> bool:
        for card in self.hand:
            if (card.get_set() == set_to_check):
                return True
        return False

    def give_card(self, card: Card) -> Card:
        if self.has_card(card):
            self.hand.remove(card)
            return card
        else:
            raise RuntimeError("This player does not have the " + str(card) + "!")

    def receive_card(self, card: Card):
        if not self.has_card(card):
            self.hand.append(card)
            self.hand = sorted(self.hand)
        else:
            raise RuntimeError("This player already has the " + str(card) + "!")
        
    def __str__(self):
        return self.name
    