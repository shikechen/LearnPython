"""
    Author: shikechen
    Function: The 52-week saving challenge
    Version: 3.0
    Date: 2019/1/31
"""
import math


def main():
    money_per_week = 10
    increase_money = 10
    total_week = 52

    total_saving = 0
    total_saving_list = []

    for i in range(total_week):
        total_saving_list.append(money_per_week)
        total_saving = math.fsum(total_saving_list)
        print('The week {} save {}, total saving is {}'.format(i + 1, money_per_week, total_saving))

        money_per_week += increase_money


if __name__ == '__main__':
    main()
