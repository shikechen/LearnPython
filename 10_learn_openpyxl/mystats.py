"""
    Author: shikechen
    Function: Read xlsx data and compute some basic statistics
    Version: 1.0
    Date: 2019/3/5
"""
import openpyxl
import statistics as stats


def main():
    book = openpyxl.load_workbook('numbers.xlsx', data_only=True)
    sheet = book.active
    rows = sheet.rows
    values = []

    for row in rows:
        for cell in row:
            values.append(cell.value)

    print('Number of values: {0}'.format(len(values)))
    print('Sum of values: {0}'.format(sum(values)))
    print('Minimum value: {0}'.format(min(values)))
    print('Maximum value: {0}'.format(max(values)))
    print('Mean: {0}'.format(stats.mean(values)))
    print('Median: {0}'.format(stats.median(values)))
    print('Standard deviation: {0}'.format(stats.stdev(values)))
    print('Variance: {0}'.format(stats.variance(values)))


if __name__ == '__main__':
    main()
