# C = Club
# S = Spade
# D = Diamonds
# H = Hearts
suits = ['C', 'S', 'D' 'H']

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def __repr__(self):
        return self.suit + str(self.val)

# keeps track of the cards, as a real life "deck" would
class Deck:
    cards = []

    def __init__(self):
        for s in suits:
            for i in range(1, 14):
                val = i
                if i == 1:
                    val = 'A'
                if i == 11:
                    val = 'J'
                if i == 12:
                    val = 'Q'
                if i == 13:
                    val = 'K'
                card = Card(s, val)
                self.cards.append(card)
