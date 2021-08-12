# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/3 13:46
@Auth ： cainiao
@File ：get_driver.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from selenium import webdriver
import appium.webdriver

import page
from time import sleep

class GetDriver:
    # 为了避免通过类名.driver来调用，只能通过get方法来获取driver
    # 搞一个私有的类属性
    __web_driver = None
    # 定义私有属性
    __app_driver = None

    # 为了能通过类名.method来调用，这里使用类方法
    @classmethod
    def get_web_driver(cls, url):
        # 如果driver为None
        if cls.__web_driver is None:
            # 获取driver
            cls.__web_driver = webdriver.Chrome()
            # 设置driver
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        return cls.__web_driver

    @classmethod
    def quit_web_driver(cls):
        if cls.__web_driver:
            cls.__web_driver.quit()
            # 这里一定记得置空操作
            cls.__web_driver = None

    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            desired_caps = {}
            desired_caps['deviceName'] = '6430d42d'
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '10'
            desired_caps['noReset'] = True
            desired_caps["appPackage"] = page.appPackage
            desired_caps["appActivity"] = page.appActivity
            cls.__app_driver = appium.webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quit()
            cls.__app_driver = None
if __name__ == '__main__':
    GetDriver.get_app_driver()
    sleep(3)
    GetDriver.quit_app_driver()
