class q_player:
    """Q-learning player"""
    
    name = "ql"


    def train(iterations=100000, lr=0.01):
        pass

    
    def move(self, game):
        if len(game.get_actions()) == 0:
            return (0, 0)