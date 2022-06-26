from random import randint, choice


class Board:
    """
    A class representing the board of the game.

    Attributes:
    -----------
    width: width of the board
    height: height of the board
    state: information about the current state of the game
    top: list containing the y-coordinate of the checker if it is 
    to be placed in column i
    valid_moves: returns the index of columns which are not full
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = [[' ']*width for i in range(height)]
        self.top = [0] * width
        self.valid_moves = list(range(width))

    def __str__(self):
        temp = [f"|{'|'.join(row)}|" for row in self.state]
        return '\n'.join(temp)

    def coords(self, col):
        return col, self.top[col]

    def place(self, col, marker):
        i, j = self.coords(col)
        self.state[self.height - j -1][i] = marker
        self.top[col] += 1

    def __getitem__(self, coords):
        x, y = coords
        return self.state[self.height - y - 1][x]


class Game:
    def __init__(self, width, height, x, players, markers = ['x', 'o']):
        self.width = width
        self.height = height
        self.x = x
        self.board = Board(width, height)
        self.turn = 1
        self.players = players
        self.markers = markers
        self.game_end = False
        self.total_turn = 0

    def check_win(self, i, j, marker):
        """
        Checks whether the piece at self.board[i][j] is a winning piece.
        """
        horizontal = lambda i, j, step: (i + step, j)
        vertical = lambda i, j, step: (i, j + step)
        diagonal = lambda i, j, step: (i + step, j + step)
        steps_counts = ((i, self.width - i - 1), (j, self.height - j - 1),
                        (min(i, j), min(self.width - i - 1, self.height - j - 1)))

        for direction, (neg_lim, pos_lim) in zip((horizontal, vertical, diagonal), steps_counts):
            temp = 1
            for step in range(1, pos_lim + 1):
                a, b = direction(i, j, step)
                if self.board[a, b] == marker:
                    temp += 1
                else:
                    # print(direction.__name__)
                    break
            for step in range(1, neg_lim + 1):
                a, b = direction(i, j, -step)
                # print(a, b, self.board[a, b])
                if self.board[a, b] == marker:
                    temp += 1
                else:
                    # print(a, b, self.board[a, b])
                    break
            if temp >= self.x:
                return True
        return False

    def step(self):
        cur_player = self.players[self.turn]
        col, marker = cur_player(self.board), self.markers[self.turn]
        i, j = self.board.coords(col)
        self.board.place(col, marker)
        if self.board.top[col] == self.height:
            self.board.valid_moves.remove(col)
        if self.check_win(i, j, marker):
            return self.turn % 2
        if self.board.valid_moves == []:
            return 'draw'
        # self.game_end = self.check_win(i, j, marker)
        self.turn = (self.turn + 1) % 2
        self.total_turn += 1
        # if (not self.game_end) and self.board.valid_moves == []:
        #     self.game_end = None

    def play(self):
        while True:
            out = self.step()
            if out in {1, 0, 'draw'}:
                # print(self.board)
                return out
            


class Player:
    def __call__(self, board):
        pass


class RandomPlayer(Player):
    def __call__(self, board:Board):
        return choice(board.valid_moves)


class DefaultGame(Game):
    def __init__(self):
        super().__init__(6, 7, 4, (RandomPlayer(), RandomPlayer()))
# for i in range(1000):
#     d = DefaultGame()
    # d.play()    

def getBoard(s):
    return [row[1:-1].split('|') for row in s.split('\n')]
