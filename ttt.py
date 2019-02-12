WIN_REWARD  =  1
LOSE_REWARD = -1
TIE_REWARD  = -1


def action_to_coor(action):
    return (action//3, action%3)


def coor_to_action(row, col):
    return row*3 + col


class game:

    state_size = 3**9
    action_size = 9

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
                    actions.append(coor_to_action(i, j))
        return actions

    
    def get_moves(self):
        actions = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    actions.append((i, j))
        return actions
    

    def get_state(self):
        """returns current state relative to player whose turn it is now"""
        # convert board to an integer in base 3 
        state = 0
        my_sym = 'x' if self.xturn else 'o'
        for i in range(3):
            for j in range(3):
                state *= 3
                if self.board[i][j] == my_sym:
                    state += 2
                elif self.board[i][j] == ' ':
                    state += 1
        return state
                    

    def act(self, action):
        if self.winner:
            # print("the game is finished")
            return
        row, col = action_to_coor(action)
        if self.board[row][col] != ' ':
            # print("error: tried to move to ({}, {}), which is occupied".format(row, col))
            return
        self.board[row][col] = 'x' if self.xturn else 'o'
        if self.check_win():
            # print("x" if self.xturn else "o", "won")
            self.winner = 'x' if self.xturn else 'o'
            return
        if len(self.get_actions()) == 0:
            self.winner = 'tie'
            return
        self.xturn = not self.xturn


    def put(self, row, col):
        if self.winner:
            # print("the game is finished")
            return
        if self.board[row][col] != ' ':
            # print("error: tried to move to ({}, {}), which is occupied".format(row, col))
            return
        self.board[row][col] = 'x' if self.xturn else 'o'
        if self.check_win():
            # print("x" if self.xturn else "o", "won")
            self.winner = 'x' if self.xturn else 'o'
            return
        if len(self.get_actions()) == 0:
            self.winner = 'tie'
            return
        self.xturn = not self.xturn
    

    def playable(self):
        return True if not self.winner else False


    def reset(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.xturn = True
        self.winner = None