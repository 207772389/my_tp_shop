# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/12 16:57
@Auth ： cainiao
@File ：read_excel.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import xlrd

def get_excel_data(index_name, my_cloums):
    """
    :param index_name: 要读取的sheet名称
    :param my_cloums: 一个sheet里要读取第几列，第一列传1，第二列传2
    :return:读取Excel某一列的数 然后返回为列表
    这里要注意：这个方法只支持行数一致的。比如有两列，但行数不一致，就会报错了。我还没解决了。
    """
    book = xlrd.open_workbook("../data/sales.xlsx")
    sheet = book.sheet_by_name(index_name)
    list = []
    for k in range(0, sheet.nrows):#返回的是行数
        value = int((sheet.row_values(k)[my_cloums - 1]))
        list.append(value)
    print(list)
    return list