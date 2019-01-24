class pg_player:
    """Policy Gradient player"""
    
    name = "pg"
    
    def move(self, game):
        if len(game.get_actions()) == 0:
            return