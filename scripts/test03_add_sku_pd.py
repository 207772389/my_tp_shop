# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/6 17:19
@Auth ： cainiao
@File ：test03_add_sku_pd.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from time import sleep

class TestAddSkuPd():

    def setup_class(self):
        #获取driver
        driver = GetDriver.get_web_driver(page.admin_url)
        #获取统一入口类
        self.page_in = PageIn(driver)
        #通过统一入口类获取登录对象，并调用登录
        self.page_in.pagein_get_PageMpLogin().pagelogin_mp_login_sucess()
        #获取页面操作对象
        self.add_pd = self.page_in.pagein_get_PageAddPd()
    def teardown_class(self):
        sleep(3)
        GetDriver.quit_web_driver()

    def test_add_sku(self):
        self.add_pd.addpd_add_sku("4", "四周班测试", "1000", "699")