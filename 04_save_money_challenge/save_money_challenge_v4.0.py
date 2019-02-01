"""
    Author: shikechen
    Function: The 52-week saving challenge
    Version: 4.0
    Date: 2019/1/31
"""
import math


def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    # global total_saving

    total_saving = 0
    total_saving_list = []

    for i in range(total_week):
        total_saving_list.append(money_per_week)
        total_saving = math.fsum(total_saving_list)
        print('The week {} save {}, total saving is {}'.format(i + 1, money_per_week, total_saving))

        money_per_week += increase_money

    return total_saving


def main():
    money_per_week = float(input('Money per week: '))
    increase_money = float(input('Increase money: '))
    total_week = int(input('Total week: '))

    total_saving = save_money_in_n_weeks(money_per_week, increase_money, total_week)
    print('Total saving: ', total_saving)


if __name__ == '__main__':
    main()
