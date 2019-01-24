import random

class react_player:
    """a player that blocks opponent's 3 in a row or takes
    3 in a row if it can, otherwise makes a random move"""
    
    name = "react"


    def block_three(self, game):
        opp_sym = 'o' if game.xturn else 'x'
        for wc in game.win_comb:
            n_opp = sum([1 if game.board[pos[0]][pos[1]] == opp_sym else 0 for pos in wc])
            if n_opp == 2:
                move = [pos if game.board[pos[0]][pos[1]] == ' ' else None for pos in wc][0]
                return move
        return None


    def put_three(self, game):
        my_sym = 'x' if game.xturn else 'o'
        for wc in game.win_comb:
            n_opp = sum([1 if game.board[pos[0]][pos[1]] == my_sym else 0 for pos in wc])
            if n_opp == 2:
                move = [pos if game.board[pos[0]][pos[1]] == ' ' else None for pos in wc][0]
                return move
        return None
    

    def move(self, game):
        if len(game.get_actions()) == 0:
            return
        move = self.block_three(game)
        if move:
            game.put(*move)
            return
        move = self.put_three(game)
        if move:
            game.put(*move)
            return
        game.put(*random.choice(game.get_actions()))
