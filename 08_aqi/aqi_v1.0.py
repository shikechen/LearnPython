"""
    Author: shikechen
    Function: Calculate AQI(Air Quality Index)
    Version: 1.0
    Date: 2019/3/9
"""


def cal_pm_iaqi(pm_val):
    pass


def cal_co_iaqi(co_val):
    pass


def cal_aqi(param_list):
    pm_value = param_list[0]
    co_value = param_list[1]
    pm_iaqi = cal_pm_iaqi(pm_value)
    co_iaqi = cal_co_iaqi(co_value)

    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(co_iaqi)

    aqi = max(iaqi_list)
    return aqi


def main():
    print('Please input data')
    input_str = input('(1)PM2.5 (2)CO:')
    str_list = input_str.split(' ')
    pm_value = float(str_list[0])
    co_value = float(str_list[1])

    param_list = []
    param_list.append(pm_value)
    param_list.append(co_value)

    aqi_value = cal_aqi(param_list)

    print('AQI: {}'.format(aqi_value))


if __name__ == '__main__':
    main()
