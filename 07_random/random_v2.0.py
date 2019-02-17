"""
    Author: shikechen
    Function: roll 2 dices
    Version: 2.0
    Date: 2019/2/17
"""
import random


def roll_dice():
    return random.randint(1, 6)


def main():
    total_times = 1000000
    result_list = [0] * 11
    roll_list = list(range(2, 13))

    roll_dict = dict(zip(roll_list, result_list))

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        for j in range(2, 13):
            if (roll1 + roll2) == j:
                roll_dict[j] += 1

    print(roll_dict)
    for i, result in roll_dict.items():
        print("count {} has {} times rate {}".format(i, result, result / total_times))


if __name__ == '__main__':
    main()
