"""
    Author: shikechen
    Function: Read Json file data and rank data and save to Json file.
    Version: 2.0
    Date: 2019/5/15
"""
import json


def process_json_file(file_path):
    f = open(file_path, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    file_path = input('Please input Json file:')
    city_list = process_json_file(file_path)
    city_list.sort(key=lambda city: city['aqi'])
    top5_list = city_list[:5]

    f = open('top5_aqi.json', mode='w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()

    print(city_list)


if __name__ == '__main__':
    main()
