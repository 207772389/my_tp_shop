# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/3 14:58
@Auth ： cainiao
@File ：read_yaml.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import yaml
import os

from config import BASE_PATH


def read_yaml(filename):
    # 组装需要读取文件的路径
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    # 定义空列表 组装测试数据
    arr = []
    # 获取文件流
    with open(file_path, "r", encoding="utf-8") as f:
        # 返回的格式是：
        # dict_values([{'username': '13812345678', 'code': '123456', 'expect': '1381234568'},
        #              {'username': '13000000', 'code': '323232', 'expect': '123333344'}])
        for datas in yaml.safe_load(f).values():
            # 这里返回的是列表嵌套列表，需要转换为列表嵌套元祖
            arr.append(tuple(datas.values()))
    return arr


if __name__ == '__main__':
    print(read_yaml("mp_login.yaml"))
