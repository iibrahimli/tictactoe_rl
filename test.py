from ttt import game
from players.user_player import *
from players.random_player import *
from players.react_player import *
from players.q_player import *
from players.deep_q_player import *
from players.pg_player import *
from players.ppo_player import *
from util import versus


player1 = react_player()
player2 = random_player()

res = versus(player1, player2, 1000)

print(res)