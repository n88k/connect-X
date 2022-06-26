from Game_Logic.game import Game, RandomPlayer
import matplotlib.pyplot as plt
import numpy as np


class Connect4(Game):
    def __init__(self, width, height) -> None:
        super().__init__(width, height, 4, (RandomPlayer(), RandomPlayer()))


width = 4
k = 1000
n = 10
result_list = []
turn_count_list = [0] * k
winrate_list = []
for i in range(k):
    results = {0: 0, 1: 0, 'draw': 0}
    cur_width, cur_height = width + i, width + 1 + i
    for j in range(n):
        game = Connect4(cur_width, cur_height)
        results[game.play()] += 1
        turn_count_list[i] += game.total_turn
    turn_count_list[i] /= n
    result_list.append(results)
    winrate_list.append(results[1]/(results[0] + results[1]))
plt.tight_layout()

x_arr = np.arange(width, width + k)
plt.plot(x_arr, turn_count_list)
a2, a1, a0 = np.polyfit(x_arr, turn_count_list, 2)
plt.plot(x_arr, a0 + x_arr * a1 + x_arr**2 * a2, label=f'Quadratic fit: y = {a0} + {a1}x + {a2}x**2')
plt.legend()
plt.show()
m, b = np.polyfit(x_arr, winrate_list, 1)
plt.plot(x_arr, x_arr * m + b, label=f'Straight line fit: y={m}x + {b}')
plt.plot(x_arr, winrate_list)
plt.legend()
plt.show()
    




