"""
    Author: shikechen
    Function: display dices, use matplotlib
    Version: 3.0
    Date: 2019/2/22
"""
import random
import matplotlib.pyplot as plt


def roll_dice():
    return random.randint(1, 6)


def main():
    total_times = 100
    result_list = [0] * 11

    roll_list = list(range(2, 13))
    roll_dict = dict(zip(roll_list, result_list))

    roll1_list = []
    roll2_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll1_list.append(roll1)
        roll2_list.append(roll2)

        for j in range(2, 13):
            if (roll1 + roll2) == j:
                roll_dict[j] += 1

    print(roll_dict)
    for i, result in roll_dict.items():
        print("count {} has {} times rate {}".format(i, result, result / total_times))

    x = range(1, total_times + 1)
    plt.scatter(x, roll1_list, alpha=0.5)
    plt.scatter(x, roll2_list, alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()
