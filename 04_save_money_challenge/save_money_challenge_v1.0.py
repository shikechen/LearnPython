"""
    Author: shikechen
    Function: The 52-week saving challenge
    Version: 1.0
    Date: 2019/1/31
"""


def main():
    money_per_week = 10
    week_index = 1
    increase_money = 10
    total_week = 52

    total_saving = 0

    while week_index <= total_week:
        total_saving += money_per_week
        print('The week {} save {}, total saving is {}'.format(week_index, money_per_week, total_saving))

        money_per_week += increase_money
        week_index += 1


if __name__ == '__main__':
    main()
