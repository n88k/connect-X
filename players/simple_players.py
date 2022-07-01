from Game_Logic.game import Board
from random import randint, choice


class Player:
    def __call__(self, board):
        pass


class RandomPlayer(Player):
    def __call__(self, board:Board):
        return choice(board.valid_moves)
