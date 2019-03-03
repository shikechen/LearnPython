"""
    Author: shikechen
    Function: display dices, use matplotlib
    Version: 4.0
    Date: 2019/2/24
"""
import random
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def roll_dice():
    return random.randint(1, 6)


def main():
    total_times = 10000

    roll_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll_list.append(roll1 + roll2)

    plt.hist(roll_list, bins=range(2, 14), normed=1, edgecolor='white', linewidth=1)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()
