"""
    Author: shikechen
    Function: Learn bar chart operation
    Version: 1.0
    Date: 2019/3/6
"""
from openpyxl import Workbook
from openpyxl.chart import (
    Reference,
    Series,
    BarChart
)


def main():
    book = Workbook()
    sheet = book.active

    rows = [
        ("USA", 46),
        ("UK", 27),
        ("China", 26),
        ("Russia", 19),
        ("Germany", 17),
        ("Japan", 12)
    ]

    for row in rows:
        sheet.append(row)

    data = Reference(sheet, min_row=1, min_col=2, max_row=6, max_col=2)
    categs = Reference(sheet, min_row=1, min_col=1, max_row=6)

    chart = BarChart()
    chart.add_data(data=data)
    chart.set_categories(categs)

    chart.legend = None
    chart.y_axis.majorGridlines = None
    chart.varyColors = True
    chart.title = 'Olympic Gold medals in Rio 2016'

    sheet.add_chart(chart, 'A8')

    book.save('bar_chart.xlsx')


if __name__ == '__main__':
    main()
