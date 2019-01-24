class deep_q_player:
    """Deep Q-learning player"""
    
    name = "dql"
    
    
    def move(self, game):
        if len(game.get_actions()) == 0:
            return