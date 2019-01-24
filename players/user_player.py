class user_player:
    """ask user to play"""
    
    name = "user"
    # user plays using numpad (remap if you don't have one)
    #  7 | 8 | 9
    #  ---------
    #  4 | 5 | 6
    #  ---------
    #  1 | 2 | 3
    controls = {'7': (0, 0), '8': (0, 1), '9': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '1': (2, 0), '2': (2, 1), '3': (2, 2)}
    

    def move(self, game):
        if game.winner or len(game.get_actions()) == 0:
            return
        game.print_board()
        pos = input("your turn: ")
        game.put(*self.controls[pos])
        print("")