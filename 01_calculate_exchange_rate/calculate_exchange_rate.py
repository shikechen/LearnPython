"""
    Author: shikechen
    Function: Convert RMB or USD according to a given exchange rate
    Version: 1.0
    Date: 2018/12/24
"""
rem_currency = 6.95

input_value = input("Please input money(Exit if input Q):")

i = 0

while input_value != 'Q':
    i = i + 1

    unit_value = input_value[-3:]
    digit_value = input_value[:-3]

    if unit_value == 'CNY':
        digit_cny = eval(digit_value)
        usd_value = digit_cny / rem_currency
        print(usd_value)

    elif unit_value == 'USD':
        digit_usd = eval(digit_value)
        cny_value = digit_usd * rem_currency
        print(cny_value)

    else:
        print("Input error!")

    input_value = input("Please input money(Exit if input Q):")

print("You are exit!")
