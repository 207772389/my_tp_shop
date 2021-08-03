# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/3 13:01
@Auth ： cainiao
@File ：test01_mp_login.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log = GetLog.get_logger()

class TestMpLogin:

    #初始化
    def setup_class(self):
        #获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        #通过统一入口类获取mp_login页面对象
        self.mp = PageIn(driver).pagein_get_PageMpLogin()


    #销毁方法
    def teardown_class(self):
        #退出driver
        GetDriver.quit_web_driver()
    #测试的业务方法
    @pytest.mark.parametrize("username,pwd,expect",read_yaml("mp_login.yaml"))
    def test_mp_login(self,username,pwd,expect):
        #调用要测试的业务方法 取得结果
        self.mp.pagelogin_mp_login(username,pwd)
        #断言返回结果是否OK
        print("\n 获取的昵称为：",self.mp.pagelogin_get_nickname())
        try:
            assert expect == self.mp.pagelogin_get_nickname()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息为：{}".format(e))
            print("错误原因：", e)
            #截图
            self.mp.base_get_img()
            #抛异常
            raise
