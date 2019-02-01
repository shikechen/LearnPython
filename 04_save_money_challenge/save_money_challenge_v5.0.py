"""
    Author: shikechen
    Function: The 52-week saving challenge
    Version: 4.0
    Date: 2019/1/31
"""
import math
import datetime


def save_money_in_n_weeks(money_per_week, increase_money, total_week):

    total_saving = 0
    week_money_list = []
    total_saving_list = []

    for i in range(total_week):
        week_money_list.append(money_per_week)
        total_saving = math.fsum(week_money_list)
        total_saving_list.append(total_saving)
        # print('The week {} save {}, total saving is {}'.format(i + 1, money_per_week, total_saving))

        money_per_week += increase_money

    return total_saving_list


def main():
    money_per_week = float(input('Money per week: '))
    increase_money = float(input('Increase money: '))
    total_week = int(input('Total week: '))

    total_saving_list = save_money_in_n_weeks(money_per_week, increase_money, total_week)

    input_date_str = input('Input date(yyyy/mm/dd): ')
    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')
    week_num = input_date.isocalendar()[1]

    print('Week {} total saving {}'.format(week_num, total_saving_list[week_num - 1]))


if __name__ == '__main__':
    main()
