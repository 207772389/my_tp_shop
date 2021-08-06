# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/5 16:37
@Auth ： cainiao
@File ：test02_add_pd.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from time import sleep

from tools.get_log import GetLog

log = GetLog.get_logger()
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
        sleep(8)
        GetDriver.quit_web_driver()
    def test_add_pd(self):
        self.add_pd.addpd_test("我是商品标题","我是商品名称","我是分享标题","我是分享描述")
        sleep(1)
        pd_name = self.add_pd.addpd_get_pd_name()
        try:
            assert "我是商品标题"==pd_name
        except Exception as e:
            #截图
            self.add_pd.base_get_screen_shot()
            #日志
            log.error("新建的商品名称：{}没有找到！！！\n 错误信息为：{}".format("我是商品名称",e))
            #抛异常
            raise

    #新建商品成功后 开始进入商品的提交审核流程
    @pytest.mark.skip(reason='这个用例还没写好，暂时不执行哈！')
    def test_pd_submit_process(self):
        pass