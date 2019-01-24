class ppo_player:
    """Proximal Policy Optimization player"""
    
    name = "ppo"
    
    def move(self, game):
        if len(game.get_actions()) == 0:
            return (0, 0)