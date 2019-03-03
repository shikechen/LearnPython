def main():
    # str = 'GitHub'
    #
    # print(str)
    # print(str[0:-1])
    # print(str[0])
    # print(str[2:5])
    # print(str[2:])
    # print(str * 2)
    # print('Hello ' + str)
    # print('--------------')
    # print('Hello\nGitHub', end='')
    # print(r'Hello\nGitHub')

    # complex_value = 2 + 3j
    # print(type(complex_value))
    # print(complex_value)
    #
    # tuple_a = ()  # empty tuple
    # tuple_b = (10)
    # tuple_c = (10,)  # tuple with only one data
    # print(type(tuple_a))
    # print(type(tuple_b))  # not tuple, is int
    # print(type(tuple_c))

    set_a = set('qwertyuiop')
    set_b = set('qsefthuko')
    print(set_a)
    print(set_b)

    print(set_a - set_b)
    print(set_a | set_b)
    print(set_a & set_b)
    print(set_a ^ set_b)
    # print()
    # help(print())

    print(print_annotation.__doc__)


def print_annotation():
    """
        This are some annotations
    """
    pass


if __name__ == '__main__':
    main()

