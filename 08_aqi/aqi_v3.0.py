"""
    Author: shikechen
    Function: Read Json file data and save to .csv file.
    Version: 3.0
    Date: 2019/5/15
"""
import json
import csv


def process_json_file(file_path):
    f = open(file_path, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    file_path = input('Please input Json file:')
    city_list = process_json_file(file_path)
    city_list.sort(key=lambda city: city['aqi'])

    lines = []
    lines.append(list(city_list[0].keys))
    for city in city_list:
        lines.append(list(city.values()))

    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()
