"""
    Author: shikechen
    Function: BMR calculator
    Version: 1.0
    Date: 2019/1/30
"""


def main():
    gender = 'M'

    weight = 60

    height = 173

    age = 27

    if gender == 'M':
        bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
    elif gender == 'F':
        bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
    else:
        bmr = -1

    if bmr != -1:
        print('BMR value: ', bmr)
    else:
        print('Not support the input value of gender')


if __name__ == '__main__':
    main()
