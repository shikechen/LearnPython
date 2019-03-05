"""
    Author: shikechen
    Function: Learn freezing panes operation
    Version: 1.0
    Date: 2019/3/5
"""
from openpyxl import Workbook


def main():
    book = Workbook()
    sheet = book.active

    sheet.freeze_panes = 'B2'

    book.save('freezing.xlsx')


if __name__ == '__main__':
    main()
