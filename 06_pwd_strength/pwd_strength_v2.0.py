"""
    Author: shikechen
    Function: Check password strength
    Version: 2.0
    Date: 2019/2/1
"""


def check_number_exist(password_str):

    has_number = False

    for n in password_str:
        if n.isnumeric():
            has_number = True
            break

    return has_number


def check_letter_exist(password_str):

    has_alpha = False

    for l in password_str:
        if l.isalpha():
            has_alpha = True
            break

    return has_alpha


def main():

    try_times = 5

    while try_times > 0:
        password = input('Input password: ')

        strength_level = 0

        # Rule 1: length >= 8
        if len(password) >= 8:
            strength_level += 1
        else:
            print('Password length too short, at least 8 digits')

        # Rule 2: contain number
        if check_number_exist(password):
            strength_level += 1
        else:
            print('Password must be contain number')

        # Rule 3: contain letter
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('Password must be contain letter')

        if strength_level == 3:
            print('Password OK')
            break
        else:
            print('Sorry')
            print()
            try_times -= 1

    if try_times <= 0:
        print("Try too many times!!!")


if __name__ == '__main__':
    main()
