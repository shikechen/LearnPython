"""
    Author: shikechen
    Function: Read file and show data
    Version: 4.0
    Date: 2019/2/7
"""


def main():
    f = open('password_3.0.txt', 'r')

    # 1 read()
    # content = f.read()
    # print(content)

    # 2 readline()
    # line = f.readline()
    # print(line)
    # line = f.readline()
    # print(line)

    # 3 readlines()
    # for line in f
    for line in f.readlines():
        print('Read: {}'.format(line))

    f.close()


if __name__ == '__main__':
    main()
