"""
    Author: shikechen
    Function: Clean data and Use Pandas lib for data visualization.
    Version: 10.0
    Date: 2019/5/14
"""
import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    aqi_data = pd.read_csv('china_cities_aqi.csv')
    print('=====Basic info=====')
    print(aqi_data.info())

    print('=====Data review=====')
    print(aqi_data.head())

    # clean data, all AQI data must > 0
    # filter_condition = aqi_data['AQI'] > 0
    # clean_aqi_data = aqi_data[filter_condition]
    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    print('Max AQI value:', clean_aqi_data['AQI'].max())
    print('Min AQI value:', clean_aqi_data['AQI'].min())
    print('Mean AQI value: ', clean_aqi_data['AQI'].mean())

    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar', x='City', y='AQI', title='空气质量最好的50个城市', figsize=(20, 10))
    plt.savefig('top50_aqi_cities_bar.png')
    plt.show()


if __name__ == '__main__':
    main()
