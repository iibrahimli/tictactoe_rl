from players.random_player import random_player
from util import versus


WIN_REWARD  =  1
LOSE_REWARD = -1
TIE_REWARD  =  0


player1 = random_player()
player2 = random_player()

res = versus(player1, player2)

print(res)