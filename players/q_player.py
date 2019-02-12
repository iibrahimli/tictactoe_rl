import numpy as np
import random
from util import *
from ttt import *
from players.random_player import random_player

class q_player:
    """Q-learning player"""
    
    name = "ql"


    def __init__(self, epsilon=0.1, alpha=0.5, gamma=0.8):
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.Q = np.zeros((game.state_size, game.action_size), dtype=np.float32)


    def train(self, iterations=100000):
        g = game()
        for i in range(iterations):
            if i % 1000 == 0:
                print("{}: {}".format(i, versus(self, random_player())))
            played = []


    def move(self, game):
        pass