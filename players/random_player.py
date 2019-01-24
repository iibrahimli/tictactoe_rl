import random

class random_player:
    """a player that makes random moves each turn"""
    
    name = "random"
    
    def move(self, game):
        # print("chose", random.choice(game.get_actions()))
        if len(game.get_actions()) == 0:
            return (0, 0)
        game.put(*random.choice(game.get_actions()))
