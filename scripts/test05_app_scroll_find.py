# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/12 14:07
@Auth ： cainiao
@File ：test05_app_scroll_find.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestAppScrollFind():
    #初始化
    def setup_class(self):
        #获取driver
        driver = GetDriver.get_app_driver()
        #获取统一入口类对象
        self.page_in = PageIn(driver)
        #通过统一入口对象调用登录方法
        self.page_in.pagein_get_PageAppLogin().applogin_login_app_success()
        #通过统一入口对象调用从右往左滑动方法
        self.app_find=self.page_in.pagein_find_PageAppFindEle()
    #结束
    def teardown_class(self):
        GetDriver.quit_app_driver()
    #测试业务方法
    def test_app_community_find_ele(self):
        self.app_find.app_find_ele("知识","腰酸背痛")