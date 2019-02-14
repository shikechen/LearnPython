"""
    Author: shikechen
    Function: learn random
    Version: 1.0
    Date: 2019/2/14
"""
import random


def roll_dice():
    return random.randint(1, 6)


def main():
    total_times = 1000000
    result_list = [0] * 6

    for i in range(total_times):
        roll_value = roll_dice()
        for j in range(1, 7):
            if roll_value == j:
                result_list[j - 1] += 1

    print(result_list)
    for i, result in enumerate(result_list):
        print("count {} has {} times rate {}".format(i+1, result, result / total_times))


if __name__ == '__main__':
    main()
