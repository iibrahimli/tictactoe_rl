from ttt import game
from players.user_player import *
from players.random_player import *
from players.react_player import *
from players.q_player import *
from players.deep_q_player import *
from players.pg_player import *
from players.ppo_player import *
from util import versus


player1 = random_player()
player2 = react_player()

res = versus(player2, player1, 1000)

print(res)