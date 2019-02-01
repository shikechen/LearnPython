"""
    Author: shikechen
    Function: Check password strength
    Version: 1.0
    Date: 2019/2/1
"""


def check_number_exist(password_str):
    for n in password_str:
        if n.isnumeric():
            return True
    return False


def check_letter_exist(password_str):
    for l in password_str:
        if l.isalpha():
            return True
    return False


def main():
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
    else:
        print('Sorry')


if __name__ == '__main__':
    main()
