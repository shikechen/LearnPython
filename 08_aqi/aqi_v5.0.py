"""
    Author: shikechen
    Function: Use requests lib to get AQI data
    Version: 5.1
    Date: 2019/5/13
"""
import requests


def get_html_text(url):
    r = requests.get(url, timeout=30)
    # print(r.status_code)
    return r.text


def main():
    city_pinyin = input('Input city\'s pinyin:')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)

    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_val = url_text[begin_index: end_index]
    print('AQI value is {}'.format(aqi_val))


if __name__ == '__main__':
    main()
