# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/12 18:19
@Auth ： cainiao
@File ：get_interval_days.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import time
def get_days(day1, day2):
    time_array1 = time.strptime(day1, "%Y-%m-%d")
    timestamp_day1 = int(time.mktime(time_array1))
    time_array2 = time.strptime(day2, "%Y-%m-%d")
    timestamp_day2 = int(time.mktime(time_array2))
    result = (timestamp_day2 - timestamp_day1) // 60 // 60 // 24
    return result + 1 #这里要注意，如果算上day1当天，就不用加1了。

if __name__ == '__main__':
    day1 = "2021-07-01"
    day2 = "2021-07-31"
    print(get_days(day1, day2))