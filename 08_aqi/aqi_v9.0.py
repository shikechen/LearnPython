"""
    Author: shikechen
    Function: Use Pandas lib to read .csv file and save processed data to .csv file.
    Version: 9.0
    Date: 2019/5/14
"""
import pandas as pd


def main():
    aqi_data = pd.read_csv('china_cities_aqi.csv')
    print('=====Basic info=====')
    print(aqi_data.info())

    print('=====Data review=====')
    print(aqi_data.head())

    print('Max AQI value:', aqi_data['AQI'].max())
    print('Min AQI value:', aqi_data['AQI'].min())
    print('Mean AQI value: ', aqi_data['AQI'].mean())

    top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    print('=====Top 10 cities=====')
    print(top10_cities)

    bottom10_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print('=====Bottom 10 cities=====')
    print(bottom10_cities)

    # Save to csv file
    top10_cities.to_csv('top10_cities.csv', index=False)
    bottom10_cities.to_csv('bottom10_cities.csv', index=False)


if __name__ == '__main__':
    main()
