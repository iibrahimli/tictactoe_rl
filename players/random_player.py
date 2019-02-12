import random

class random_player:
    """a player that makes random moves each turn"""
    
    name = "random"
    

    def move(self, game):
        if len(game.get_moves()) != 0:
            game.put(*random.choice(game.get_moves()))