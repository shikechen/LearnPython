"""
    Author: shikechen
    Function: Draw fractal tree
    Version: 1.0
    Date: 2019/1/13
"""

import turtle


def draw_branch(branch_length):
    if branch_length > 5:
        # draw right branch
        turtle.forward(branch_length)
        print('forward', branch_length)
        turtle.right(20)
        print('right 20')
        draw_branch(branch_length - 15)

        # draw left branch
        turtle.left(40)
        print('left 40')
        draw_branch(branch_length - 15)

        # return
        turtle.right(20)
        print('right 20')
        turtle.backward(branch_length)
        print('backward', branch_length)


def main():
    """
        main method
    """
    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    draw_branch(100)
    turtle.exitonclick()


if __name__ == '__main__':
    main()