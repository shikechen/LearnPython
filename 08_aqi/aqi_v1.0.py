"""
    Author: shikechen
    Function: Calculate AQI(Air Quality Index)
    Version: 1.0
    Date: 2019/3/9
"""


def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi


def cal_pm_iaqi(pm_val):
    if 0 <= pm_val < 36:
        iaqi = cal_linear(0, 50, 0, 35, pm_val)
    elif 36 <= pm_val < 76:
        iaqi = cal_linear(50, 100, 35, 75, pm_val)
    elif 76 <= pm_val < 116:
        iaqi = cal_linear(100, 150, 75, 115, pm_val)
    elif 116 <= pm_val < 151:
        iaqi = cal_linear(150, 200, 115, 150, pm_val)
    elif 151 <= pm_val < 251:
        iaqi = cal_linear(200, 300, 150, 250, pm_val)
    elif 251 <= pm_val < 351:
        iaqi = cal_linear(300, 400, 250, 350, pm_val)
    elif 351 <= pm_val < 501:
        iaqi = cal_linear(400, 500, 350, 500, pm_val)

    return iaqi


def cal_co_iaqi(co_val):
    if 0 <= co_val < 3:
        iaqi = cal_linear(0, 50, 0, 2, co_val)
    elif 3 <= co_val < 5:
        iaqi = cal_linear(50, 100, 2, 4, co_val)
    elif 5 <= co_val < 15:
        iaqi = cal_linear(100, 150, 4, 14, co_val)
    elif 15 <= co_val < 25:
        iaqi = cal_linear(150, 200, 14, 24, co_val)
    elif 25 <= co_val < 37:
        iaqi = cal_linear(200, 300, 24, 36, co_val)
    elif 37 <= co_val < 49:
        iaqi = cal_linear(300, 400, 36, 48, co_val)
    elif 49 <= co_val < 61:
        iaqi = cal_linear(400, 500, 48, 60, co_val)

    return iaqi


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
