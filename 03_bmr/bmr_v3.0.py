"""
    Author: shikechen
    Function: BMR calculator
    Version: 3.0
    Date: 2019/1/30
"""


def main():

    y_or_n = input('Want to quit(Y/n)?: ')

    while y_or_n != 'Y':

        print('Input value(use blank to divide)')
        input_str = input('Gender(M/F) Weight(kg) Height(cm) Age: ')
        input_str_list = input_str.split(' ')

        gender = input_str_list[0]
        # print(type(gender))

        weight = float(input_str_list[1])
        # print(type(weight))

        height = float(input_str_list[2])

        age = int(input_str_list[3])

        if gender == 'M':
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == 'F':
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print('Your Gender:{}, Weight:{}kg, Height:{}cm, Age:{} years old'.format(gender, weight, height, age))
            print('And your BMR value: {} kcal'.format(bmr))
        else:
            print('Not support the input value of gender')

        print()
        y_or_n = input('Want to quit(y/N)?: ')


if __name__ == '__main__':
    main()
