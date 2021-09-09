# -*- coding: utf-8 -*-
"""
@Time ： 2021/5/27 16:38
@Auth ： cainiao
@File ：read_json.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import json

def read_json(filename):
    filepath = "../data/"+filename
    with open(filepath,"r",encoding="utf-8")as f:
        """
        {'add_001': {'num1': 1, 'num2': 2, 'expect': 3}, 
        'add_002': {'num1': 11, 'num2': 22, 'expect': 33}, 
        'add_003': {'num1': 1, 'num2': 1, 'expect': 3}, 
        'add_004': {'num1': 1, 'num2': 12, 'expect': 3}}
        """
        # 这是拿到的json格式，但我们需要的格式是[(),(),()]，需要经过以下处理：
        datas = json.load(f)
        arrys = []
        for data in datas.values():
            arrys.append((data["num1"], data["num2"], data["expect"]))
        print(arrys)
        return arrys

if __name__ == '__main__':
    datas = read_json("cal_add.json")
    print(datas)
    arrys=[]
    for data in datas.values():
        # arrys.append(data)
        arrys.append((data["num1"],data["num2"],data["expect"]))
    print(arrys)