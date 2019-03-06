"""
    Author: shikechen
    Function: Write image to sheet
    Version: 1.0
    Date: 2019/3/6
"""
from openpyxl import Workbook
from openpyxl.drawing.image import Image


def main():
    book = Workbook()
    sheet = book.active

    img = Image('dream_lake_colorado.png')
    sheet['A1'] = 'Beautiful scenery'

    sheet.add_image(img, 'B2')

    book.save('sheet_image.xlsx')


if __name__ == '__main__':
    main()
