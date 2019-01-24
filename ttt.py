WIN_REWARD  =  1
LOSE_REWARD = -1
TIE_REWARD  =  0

class game:

    # winning combinations
    win_comb = [((0, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (1, 2)),
                ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)),
                ((0, 2), (1, 1), (2 ,0))]
    
    
    def __init__(self):
        """creates an empty game board"""
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.xturn = True
        self.winner = None
    
    
    def print_board(self):
        print(self.board[0][0], self.board[0][1], self.board[0][2], sep=' | ')
        print("---------")
        print(self.board[1][0], self.board[1][1], self.board[1][2], sep=' | ')
        print("---------")
        print(self.board[2][0], self.board[2][1], self.board[2][2], sep=' | ')
    
    
    def check_win(self):
        for player in ['x', 'o']:
            for c in self.win_comb:
                if self.board[c[0][0]][c[0][1]] == player and \
                   self.board[c[1][0]][c[1][1]] == player and \
                   self.board[c[2][0]][c[2][1]] == player:
                    return True
    
    
    def get_actions(self):
        actions = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    actions.append((i, j))
        return actions

    
    def put(self, posf, poss):
        if self.winner:
            # print("the game is finished")
            return
        if self.board[posf][poss] != ' ':
            # print("error: tried to move to ({}, {}), which is occupied".format(posf, poss))
            return
        self.board[posf][poss] = 'x' if self.xturn else 'o'
        if self.check_win():
            # print("x" if self.xturn else "o", "won")
            self.winner = 'x' if self.xturn else 'o'
            return
        if len(self.get_actions()) == 0:
            self.winner = 'tie'
            return
        self.xturn = not self.xturn
    
    
    def get_state(self):
        """returns current state relative to player whose turn it is now"""
        res = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    res.append(0)
                elif self.board[i][j] == 'x':
                    res.append(1 if self.xturn else -1)
                else:
                    res.append(-1 if self.xturn else 1)
        return res
    
    
    def reset(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.xturn = True
        self.winner = None