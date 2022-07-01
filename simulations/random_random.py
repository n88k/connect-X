from Game_Logic.game import Game
from players import *


class Connect4(Game):
    def __init__(self, width, height) -> None:
        super().__init__(width, height, 4, (RandomPlayer(), RandomPlayer()))


Connect4(6, 7).play(True, 1)