"""
    Author: shikechen
    Function: Intelligence process Json or csv file.
    Version: 4.0
    Date: 2019/5/15
"""
import json
import csv
import os


def process_json_file(file_path):
    # f = open(file_path, mode='r', encoding='utf-8')
    # city_list = json.load(f)
    # return city_list
    with open(file_path, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)


def process_csv_file(file_path):
    with open(file_path, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row))


def main():
    file_path = input('Please input file name:')
    file_name, file_ext = os.path.splitext(file_path)

    if file_ext == '.json':
        process_json_file(file_path)
    elif file_ext == '.csv':
        process_csv_file(file_path)
    else:
        print('No support such file!')


if __name__ == '__main__':
    main()
