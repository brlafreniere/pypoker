from player import Player
from game import Game

def run():
    num_ai_players = int(input("How many AI players? "))
    game = Game(num_ai_players=num_ai_players)

run()
