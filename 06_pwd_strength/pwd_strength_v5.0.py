"""
    Author: shikechen
    Function: def password class
    Version: 5.0
    Date: 2019/2/7
"""


class PasswordTool:
    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def process_password(self):
        # Rule 1: length >= 8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('Password length too short, at least 8 digits')

        # Rule 2: contain number
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('Password must be contain number')

        # Rule 3: contain letter
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('Password must be contain letter')

    def check_number_exist(self):

        has_number = False

        for n in self.password:
            if n.isnumeric():
                has_number = True
                break

        return has_number

    def check_letter_exist(self):

        has_alpha = False

        for l in self.password:
            if l.isalpha():
                has_alpha = True
                break

        return has_alpha


def main():

    try_times = 5

    while try_times > 0:
        password = input('Input password: ')

        # init class
        password_tool = PasswordTool(password)
        # invoke class method
        password_tool.process_password()

        strength_level_str = ''
        if password_tool.strength_level == 3:
            strength_level_str = 'High'
        elif password_tool.strength_level == 2:
            strength_level_str = 'Middle'
        elif password_tool.strength_level == 1:
            strength_level_str = 'Low'
        else:
            strength_level_str = 'Floor'

        # write file
        f = open('password_5.0.txt', 'a')
        f.write('Pwd: {}, strength_level: {}\n'.format(password, strength_level_str))
        f.close()

        if password_tool.strength_level == 3:
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
