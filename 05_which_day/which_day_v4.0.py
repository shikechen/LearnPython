"""
    Author: shikechen
    Function: Which day? use dict.
    Version: 4.0
    Date: 2019/2/1
"""
from datetime import datetime


def is_leap_year(year):

    is_leap = False

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True

    return is_leap


def main():
    input_date_str = input('Input date(yyyy/mm/dd): ')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    month_days_dict = {1: 31,
                       2: 28,
                       3: 31,
                       4: 30,
                       5: 31,
                       6: 30,
                       7: 31,
                       8: 31,
                       9: 30,
                       10: 31,
                       11: 30,
                       12: 31}

    # days_month_dict = {30: {4, 6, 9, 11},
    #                    31: {1, 3, 5, 7, 8, 10, 12}}

    # _30_days_month_set = {4, 6, 9, 11}
    # _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}
    days = 0
    days += day

    for i in range(1, month):
        days += month_days_dict[i]

        # if i in _30_days_month_set:
        #     days += 30
        # elif i in _31_days_month_set:
        #     days += 31
        # else:
        #     days += 28

    if is_leap_year(year) and month > 2:
        days += 1

    print('This is the {} day of year {}'.format(days, year))


if __name__ == '__main__':
    main()
