# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/5 16:37
@Auth ： cainiao
@File ：test02_add_pd.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from time import sleep

class TestAddPd:

    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.admin_url)
        # 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 通过统一入口对象获取登录操作并登录成功
        self.page_in.pagein_get_PageMpLogin().pagelogin_mp_login_sucess()
        # 获取新增商品页面对象
        self.add_pd = self.page_in.pagein_get_PageAddPd()

    def teardown_class(self):
        sleep(3)
        GetDriver.quit_web_driver()
    def test_add_pd(self):
        self.add_pd.addpd_test("我是商品标题")