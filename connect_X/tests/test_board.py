import pytest
from Game_Logic.game import *


def test_place_get():
    board = Board(4, 3)
    for i in range(board.width):
        board.place(i, 'x')
    for i in range(board.width):
        board[i, 0] == 'x'

def test_cooeds():
    board = Board(4, 3)
    assert board.coords(2) == (2, 0)
    board.place(2,'x')
    assert board.coords(2) == (2, 1)
