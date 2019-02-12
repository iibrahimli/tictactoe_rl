from ttt import game
from players.user_player import user_player
from players.random_player import random_player
from players.react_player import react_player
from players.q_player import q_player
from players.deep_q_player import deep_q_player
from players.pg_player import pg_player
from players.ppo_player import ppo_player
from util import versus


# player1 = react_player()
# player2 = random_player()
# versus(player1, player2, 100)

qpl = q_player()
qpl.train(200000)

versus(qpl, random_player())

# versus(qpl, user_player(), 3)