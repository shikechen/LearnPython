"""
    Author: shikechen
    Function: Millionaire
    Version: 1.0
    Date: 2019/3/20
"""


def main():
    principal = 10000
    # +10%
    every_day_increase = 0.1
    total_business_day_of_a_year = 200

    total_money = principal

    day_index = 1
    print('In day 1 total money is {} RMB'.format(total_money))
    while day_index <= total_business_day_of_a_year:
        total_money = total_money * (1 + every_day_increase)
        day_index += 1
        print('In day {} total money is {} RMB'.format(day_index, total_money))


if __name__ == '__main__':
    main()
