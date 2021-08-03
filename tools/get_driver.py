# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/3 13:46
@Auth ： cainiao
@File ：get_driver.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from selenium import webdriver


class GetDriver:
    #为了避免通过类名.driver来调用，只能通过get方法来获取driver
    #搞一个私有的类属性
    __driver = None

    #为了能通过类名.method来调用，这里使用类方法
    @classmethod
    def get_web_driver(cls,url):
        #如果driver为None
        if cls.__driver is None:
            #获取driver
            cls.__driver = webdriver.Chrome()
            #设置driver
            cls.__driver.maximize_window()
            #打开url
            cls.__driver.get(url)
        return cls.__driver

    @classmethod
    def quit_web_driver(cls):
        if cls.__driver:
            cls.__driver.quit()
            #这里一定记得置空操作
            cls.__driver=None
