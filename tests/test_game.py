import pytest
from Game_Logic.game import RandomPlayer, Game, getBoard

def test_check_win():
    game = Game(5, 7, 2, (RandomPlayer(), RandomPlayer()))
    b = game.board
    b.place(2, 'x')
    for i in range(3):
        b.place(2, 'o')
    assert game.check_win(2, 3, 'o')

    s = """| | | | | | |
| | |o| | | |
|x| |o| | |x|
|o| |o| | |x|
|x| |x| |o|o|
|x| |o| |x|x|
|o|x|o| |x|o|"""
    game.board.state = getBoard(s)
    assert game.check_win(2, 5, 'o')


def test_check_win_bottom():
    game = Game(5, 7, 2, (RandomPlayer(), RandomPlayer()))
    b = game.board
    b.place(1, 'x')
    assert not game.check_win(1, 0, 'x')

    b.place(3, 'o')
    b.place(4, 'o')
    assert game.check_win(4, 0, 'o')


def test_check_win_bottom_left():
    game = Game(5, 7, 2, (RandomPlayer(), RandomPlayer()))
    b = game.board
    b.place(0, 'x')
    assert not game.check_win(0, 0, 'x')

def test_check_win_bottom_right():
    game = Game(5, 7, 2, (RandomPlayer(), RandomPlayer()))
    b = game.board
    b.place(4, 'x')
    assert not game.check_win(4, 0, 'x')
    b.place(3,'x')
    assert game.check_win(3, 0, 'x')

def test_check_win_diag_corner():
    game = Game(6, 6, 2, (RandomPlayer(), RandomPlayer()))
    b = game.board
    b.place(0, 'x')
    b.place(1, 'o')
    b.place(1, 'x')
    assert game.check_win(1, 1, 'x')

    game.board.state = getBoard("""| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| |x| | | | |
| |o|x|x|o| |
| |o|x|x|o|o|""")

    assert game.check_win(1, 2, 'x')


