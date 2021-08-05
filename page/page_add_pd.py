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


class PageAddPd(WebBase):

    #点击 新建
    def addpd_click_add_btn(self):
        self.base_click(page.pd_list_add_btn)

    #输入商品标题
    def addpd_input_pd_title(self,value):
        sleep(1)
        self.base_input(page.pd_adding_pd_title,value,ele = 2)
    #选择商品类型
    def addpd_choose_pd_type(self):
        # 先点击输入框
        self.base_click(page.pd_adding_pd_type)
        #从下拉列表选择服务类
        self.base_click(page.pd_adding_pd_typevalue)

    #选择预热时间
    def addpd_choose_time(self):
        #先点击日期弹框
        self.base_click(page.pd_adding_click_data)
        #从弹出的日期选择器里选择开始和结束时间 注意：这里的结束时间目前是固定选择最后一个日期的，还没有更好的方案
        self.base_click(page.pd_adding_start_data)
        self.base_click(page.pd_adding_end_data)
        #点击确定
        self.base_click(page.pd_adding_date_ok)

    #选择用户评价
    def addpd_choose_evaluation(self):
        self.base_click(page.pd_adding_evluation)

    #输入商品名称
    def addpd_input_pd_name(self):
        self.base_input(page.pd_adding_pd_name,"我是商品名称",3)

    #输入分享标题
    def addpd_input_share_title(self):
        self.base_input(page.pd_adding_share_title)

    #输入分享描述
    def addpd_input_share_info(self):
        self.base_input(page.pd_adding_share_info)

    #保存按钮
    def addpd_click_save_btn(self):
        self.base_click(page.pd_adding_save_btn)



    #业务组合方法
    def addpd_test(self,value):
        self.base_click(page.pd_list_add_btn)
        self.addpd_input_pd_title(value)
        self.addpd_choose_pd_type()
        self.addpd_choose_time()
        self.addpd_choose_evaluation()
        self.addpd_input_pd_name()
        self.addpd_input_share_title()
        self.addpd_input_share_info()
        self.addpd_click_save_btn()