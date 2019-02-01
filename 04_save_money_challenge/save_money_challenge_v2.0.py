"""
    Author: shikechen
    Function: The 52-week saving challenge
    Version: 2.0
    Date: 2019/1/31
"""
import math


def main():
    money_per_week = 10
    week_index = 1
    increase_money = 10
    total_week = 52

    total_saving = 0
    total_saving_list = []

    while week_index <= total_week:
        # total_saving += money_per_week

        total_saving_list.append(money_per_week)
        total_saving = math.fsum(total_saving_list)
        print('The week {} save {}, total saving is {}'.format(week_index, money_per_week, total_saving))

        money_per_week += increase_money
        week_index += 1


if __name__ == '__main__':
    main()
