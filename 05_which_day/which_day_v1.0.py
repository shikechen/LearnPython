"""
    Author: shikechen
    Function: Which day
    Version: 1.0
    Date: 2019/1/31
"""
from datetime import datetime


def main():
    input_date_str = input('Input date(yyyy/mm/dd): ')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    days_in_month_tuple = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    print(days_in_month_tuple[: month - 1])
    days = sum(days_in_month_tuple[: month - 1]) + day

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        if month > 2:
            # leap year
            print('leap year')
            days += 1

    print('This is the {} day of year {}'.format(days, year))


if __name__ == '__main__':
    main()
