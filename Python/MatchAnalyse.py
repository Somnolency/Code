from random import random

def print_info():
    print('这个程序模拟两个选手A和B的某种竞技比赛')
    print('程序运行需要A和B的能力值(以0到1的小数表示)')

def get_inputs():
    a = eval(input('请输入选手A的能力值（0-1）：'))
    b = eval(input("请输入选手B的能力值（0-1）："))
    n = eval(input('模拟比赛的场次：'))
    return a, b, n

def print_summary(win_a, win_b):
    n = win_a + win_b
    print('竞技分析开始，共模拟{}场比赛'.format(n))
    print('选手A获胜{}场比赛，占比{:0.1%}'.format(win_a, win_a/n))
    print('选手B获胜{}场比赛，占比{:0.1%}'.format(win_b, win_b/n))

def game_over(score_a, score_b):
    return score_a == 15 or score_b == 15

def sim_games(n, prob_a, prob_b):
    wins_a, wins_b = 0, 0
    for i in range(n):
        score_a, score_b = sim_game(prob_a, prob_b)
        if score_a > score_b:
            wins_a += 1
        else:
            wins_b += 1
    return wins_a, wins_b

def sim_game(prob_a, prob_b):
    score_a, score_b = 0, 0
    serving = 'a'
    while not game_over(score_a, score_b):
        if serving == 'a':
            if random() < prob_a:
                score_a += 1
            else:
                serving = 'b'
        else:
            if random() < prob_b:
                score_b += 1
            else:
                serving = 'a'
    return score_a, score_b



def main():
    print_info()
    prob_a, prob_b, n = get_inputs()
    wins_a, wins_b = sim_games(n, prob_a, prob_b)
    print_summary(wins_a, wins_b)

main()