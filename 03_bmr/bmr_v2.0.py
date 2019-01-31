"""
    Author: shikechen
    Function: BMR calculator
    Version: 2.0
    Date: 2019/1/30
"""


def main():

    y_or_n = input('Want to quit(Y/n)?: ')

    while y_or_n != 'Y':
        gender = input('Gender(M/F): ')
        # print(type(gender))

        weight = float(input('Weight(kg): '))
        # print(type(weight))

        height = float(input('Height(cm): '))

        age = int(input('Age: '))

        if gender == 'M':
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == 'F':
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print('BMR value(kcal): ', bmr)
        else:
            print('Not support the input value of gender')

        print()
        y_or_n = input('Want to quit(y/N)?: ')


if __name__ == '__main__':
    main()
