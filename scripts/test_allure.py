# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/6 15:48
@Auth ： cainiao
@File ：test_allure.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import allure

"""@allure.feature # 用于定义被测试的功能，被测产品的需求点
@allure.story # 用于定义被测功能的用户场景，即子功能点
with allure.step # 用于将一个测试用例，分成几个步骤在报告中输出
allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
@pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤"""


@allure.step("步骤1，打开百度")
def step1():
    print("111")


@allure.step("步骤2，输入关键字")
def step2():
    print("222")


@allure.feature("搜索")
class TestAllure:
    @allure.story("百度搜索")
    def test1(self):
        """这是测试百度搜索"""
        step1()
        step2()
        print("百度一下，你就知道")

    def test2(self):
        """这是测试谷歌搜索"""
        assert 1 == 2, "搜索失败"
