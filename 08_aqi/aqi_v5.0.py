"""
    Author: shikechen
    Function: Use requests lib to get AQI data
    Version: 5.0
    Date: 2019/5/13
"""
import requests


def get_html_text(url):
    r = requests.get(url, timeout=30)
    print(r.status_code)
    return r.text


def main():
    city_pinyin = input('Input city\'s pinyin:')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)
    print(url_text)


if __name__ == '__main__':
    main()
