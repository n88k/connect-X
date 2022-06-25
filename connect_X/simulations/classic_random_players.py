from Game_Logic.game import DefaultGame


# print('hi')
n = 10000
score = {0 : 0, 1 : 0, None : 0}
for i in range(n):
    # print('hi')
    winner = DefaultGame().play()
    score[winner] += 1
print(score)



