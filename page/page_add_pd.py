# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/5 16:31
@Auth ： cainiao
@File ：page_add_pd.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import page
from base.web_base import WebBase
from time import sleep

from tools.get_log import GetLog

log = GetLog.get_logger()


class PageAddPd(WebBase):

    # 点击 新建
    def addpd_click_add_btn(self):
        self.base_click(page.pd_list_add_btn)

    # 输入商品标题
    def addpd_input_pd_title(self, pdtitle):
        sleep(1)
        self.base_input(page.pd_adding_pd_title, pdtitle, ele=2)

    # 选择商品类型
    def addpd_choose_pd_type(self):
        # 先点击输入框
        self.base_click(page.pd_adding_pd_type)
        # 从下拉列表选择服务类
        self.base_click(page.pd_adding_pd_typevalue)

    # 选择预热时间
    def addpd_choose_time(self):
        # 先点击日期弹框
        self.base_click(page.pd_adding_click_data)
        # 从弹出的日期选择器里选择开始和结束时间 注意：这里的结束时间目前是固定选择最后一个日期的，还没有更好的方案
        self.base_click(page.pd_adding_start_data)
        self.base_click(page.pd_adding_end_data)
        # 点击确定
        self.base_click(page.pd_adding_date_ok)

    # 选择用户评价
    def addpd_choose_evaluation(self):
        self.base_click(page.pd_adding_evluation)

    # 输入商品名称
    def addpd_input_pd_name(self, value):
        self.base_input(page.pd_adding_pd_name, value, 3)

    # 输入分享标题
    def addpd_input_share_title(self, value):
        self.base_input(page.pd_adding_share_title,value)

    # 输入分享描述
    def addpd_input_share_info(self, value):
        self.base_input(page.pd_adding_share_info,value)

    # 保存按钮
    def addpd_click_save_btn(self):
        self.base_click(page.pd_adding_save_btn)

    #确认弹框上的确认按钮
    def addpd_click_makesure_ok(self):
        self.base_click(page.pd_adding_makesure_ok)

    # 业务组合方法
    def addpd_test(self, pdtitle, pdname, sharetitle, shareinfo):
        log.info("正在调用新增商品的业务组合方法")
        self.base_click(page.pd_list_add_btn)
        self.addpd_input_pd_title(pdtitle)
        self.addpd_choose_pd_type()
        self.addpd_choose_time()
        self.addpd_choose_evaluation()
        self.addpd_input_pd_name(pdname)
        self.addpd_input_share_title(sharetitle)
        self.addpd_input_share_info(shareinfo)
        self.addpd_click_save_btn()
        self.addpd_click_makesure_ok()

    # 新增商品后回到商品列表，先点击状态，选择编辑中，获取第一个编辑的商品即为新增的商品
    def addpd_click_status(self):
        log.info("正在切换状态。。。")
        # 先点击状态
        self.base_click(page.pd_list_status)
        # 下拉框中选择 编辑中
        self.base_click(page.pd_list_choose_status, 1)

    # 新增商品后 获取待编辑中的商品名称 给断言用
    def addpd_get_pd_name(self):
        log.info("正在获取商品列表的商品名称")
        # 先调用上面的方法把状态切换为 编辑中
        self.addpd_click_status()
        return self.base_get_text(page.pd_list_pd_name, 3)

    # 切换状态为编辑中 点击提交审批
    def addpd_submit_sp(self):
        #切换到编辑中
        pass

        #点击提交审批

    # 切换状态为待审批 然后点击通过按钮
    def addpd_submit_pass(self):
        pass

    # 切换状态为待上架 然后点击上架按钮
    def addpd_submit_up(self):
        pass

    # 切换状态为已上架 然后点击已下架按钮
    def addpd_submit_down(self):
        pass

    # 提交流程来个业务组合
    def addpd_test_submit_process(self):
        self.addpd_submit_sp()
        self.addpd_submit_pass()
        self.addpd_submit_up()
        self.addpd_submit_down()
