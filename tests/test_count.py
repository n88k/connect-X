import enum
from Game_Logic.game import *


def place_list(board:Board, l, markers=['x', 'o']):
    for index, col in enumerate(l):
        board.place(col, markers[index % len(markers)])

def test_count():
    game = Game(6, 7, 4, (RandomPlayer(), RandomPlayer()))
    b = game.board
    place_list(b, [1, 3, 2, 2])
    assert game.consecutive_count(2, 0, 'x') == 2
    assert game.consecutive_count(3, 0, 'o') == 2
    place_list(b, [3, 4, 4, 5, 4, 0])
    assert game.consecutive_count(3, 1, 'x') == 3
    assert game.consecutive_count(4, 0, 'o') == 3
    place_list(b, [0, 1])
    assert game.consecutive_count(0, 0, 'o') == 2
    print(b)

test_count()