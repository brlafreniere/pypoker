from deck import Deck
from player import Player

# keeps track of everything basically, used kind of as a universal reference to
# other objects
class Game:
    def __init__(self, num_ai_players):
        self.ai_players = []
        self.human_player = Player(ai=False)
        self.deck = Deck()

        for i in range(num_ai_players):
            self.ai_players.append(Player())
