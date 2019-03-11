"""
    Author: shikechen
    Function: Company staff meal report intelligent statistical system
    Version: 1.1
    Date: 2019/3/11
"""
import openpyxl


def main():
    excel_name = '2019_2.xlsx'
    book = openpyxl.load_workbook(excel_name)
    sheet_name_list = book.sheetnames
    print(sheet_name_list)

    for sheet_name in sheet_name_list:
        print('sheet name: ', sheet_name)
        if sheet_name.__contains__('-'):
            sheet = book[sheet_name]
            print('sheet title: ', sheet.title)

            rows = sheet.rows

            sheet_max_row = sheet.max_row
            print('sheet_max_row', sheet_max_row)
            sheet_max_column = sheet.max_column
            print('sheet_max_column', sheet_max_column)

            row_index = 0
            column_write_index = sheet_max_column + 1
            for row in rows:
                row_sum = 0
                row_index += 1

                # the first row is title
                if row_index > 1:
                    for cell in row:
                        cell_value = cell.value
                        # print(cell_value)

                        cell_sum = 0

                        if isinstance(cell_value, str):
                            if '早餐' in cell_value:
                                cell_sum += 5

                            if '午餐' in cell_value:
                                cell_sum += 15

                            if '晚餐' in cell_value:
                                cell_sum += 10

                        row_sum += cell_sum

                    sheet.cell(row=row_index, column=column_write_index).value = row_sum

    book.save(excel_name)
    book.close()


if __name__ == '__main__':
    main()
