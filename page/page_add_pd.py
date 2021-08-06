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
        self.base_input(page.pd_adding_share_title, value)

    # 输入分享描述
    def addpd_input_share_info(self, value):
        self.base_input(page.pd_adding_share_info, value)

    # 保存按钮
    def addpd_click_save_btn(self):
        self.base_click(page.pd_adding_save_btn)

    # 确认弹框上的确认按钮
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
        # self.addpd_click_status()
        return self.base_get_text(page.pd_list_pd_name, 3)

    """至此，商品新建成功了，以下开始新建sku"""

    # 新增商品后 开始新增sku，点击sku管理按钮
    def addpd_click_addsku_manage(self):
        log.info("开始新建新建sku了")
        self.base_click(page.pd_list_sku_manage, 1)

    # 进入新增sku界面,点击 新建sku
    def addpd_click_addsku(self):
        self.base_click(page.pd_list_add_sku)

    # 进入新增sku
    def addpd_click_addsku_btn(self):
        self.base_click(page.pd_list_addsku_btn)

    # 进入sku输入页面 开始编辑操作
    def addpd_input_sku_period(self, period):
        self.base_input(page.pd_list_addsku_period, period)

    # 选择开营时间
    def addpd_choose_sku_starttime(self):
        # 先点击弹出选择器
        self.base_click(page.pd_list_addsku_starttime_btn)
        # 再点击选择日期
        self.base_click(page.pd_list_addsk_choose_starttime)
        # 再点击选择器上的确定按钮
        self.base_click(page.pd_list_addsku_starttime_ok)

    # 输入sku名称
    def addpd_input_skuname(self, skuname):
        self.base_input(page.pd_list_addsku_skuname, skuname)

    # 输入原价
    def addpd_input_origin_price(self, originprice):
        self.base_input(page.pd_list_addsku_originprice, originprice)

    # 输入特价
    def addpd_input_especial_price(self, especialprice):
        self.base_input(page.pd_list_addsku_especialprice, especialprice)

    # 点击上面的保存按钮
    def addpd_addsku_first_savebtn(self):
        self.base_click(page.pd_list_addsku_first_savebtn)

    # 点击下面的保存按钮
    def addpd_addsku_second_savebtn(self):
        log.info("sku新建成功了，sku is done!")
        self.base_click(page.pd_list_addsku_second_savebtn)

    """至此，sku就新建完成了，返回到了sku列表页面，以下开始提交sku到上架状态"""

    # 点击提交审批
    def addpd_skulist_click_sp(self):
        sleep(1)
        self.base_click(page.pd_list_addsku_skulist_sp)

    # 审批通过后 点击通过
    def addpd_skulist_click_pass(self):
        sleep(1)
        self.base_click(page.pd_list_addsku_skulist_pass_sp)

    # 通过后，就点击上架了
    def addpd_skulist_click_sj(self):
        log.info("恭喜，sku已经成功上架了！！！")
        sleep(1)
        self.base_click(page.pd_list_addsku_skulist_sj)

    """至此，sku状态变为上架了，点击 商品列表 回到商品列表页面，开始把商品状态变为上架"""

    # 点击左边导航栏的 商品列表
    def addpd_click_pdlist(self):
        self.base_click(page.pd_list_click_pdlist)

    # 点击商品后面的提交审批开始审批流程了 点击 提交审批
    def addpd_pdlist_click_sp(self):
        sleep(1)
        self.base_click(page.pd_list_submit_sp, 2)

    # 审批后，点击通过
    def addpd_pdlist_click_pass(self):
        sleep(1)
        self.base_click(page.pd_list_click_pass, 2)

    # 通过后，点击上架
    def addpd_pdlist_click_sj(self):
        sleep(1)
        log.info("商品成功上架了")
        self.base_click(page.pd_list_click_sj, 2)

    # 添加sku业务方法+商品提交上架 组合
    def addpd_add_sku(self, period, skuname, originprice, especialprice):
        """

        :param period: sku的开营周期
        :param skuname: sku的名称
        :param originprice: sku的原价
        :param especialprice: sku的特价
        :return:
        """
        self.addpd_click_addsku_manage()
        self.addpd_click_addsku()
        self.addpd_click_addsku_btn()
        self.addpd_input_sku_period(period)
        self.addpd_choose_sku_starttime()
        self.addpd_input_skuname(skuname)
        self.addpd_input_origin_price(originprice)
        self.addpd_input_especial_price(especialprice)
        self.addpd_addsku_first_savebtn()
        self.addpd_addsku_second_savebtn()
        self.addpd_skulist_click_sp()
        self.addpd_skulist_click_pass()
        self.addpd_skulist_click_sj()
        self.addpd_click_pdlist()
        self.addpd_pdlist_click_sp()
        self.addpd_pdlist_click_pass()
        self.addpd_pdlist_click_sj()

    #商品上架后 获取商品的上架状态》断言时调用
    def addpd_get_pd_status(self):
        return self.base_get_text(page.pd_list_get_pd_status)