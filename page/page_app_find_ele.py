# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/11 13:04
@Auth ： cainiao
@File ：page_app_find_ele.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import page
from base.app_base import AppBase
from time import sleep


class PageAppFindEle(AppBase):
    #进入APP后 先点击底部 社区 tab
    def app_click_tab_community(self):
        self.base_click(page.app_tab_community)
    #先滑动顶部区域来查找对应的频道tab
    def app_findele_click_channel(self,click_text):
        sleep(1)
        self.app_base_right_wipe_left(page.app_community_up_scroll,click_text)
    #点击频道后 在频道对应的页面内容里 上下滑动 来找具体的页面内容
    def app_findele_search_page(self,click_text):
        sleep(1)
        self.app_base_down_wipe_up(page.app_community_middle_area,click_text)
    #组合上面两个步骤 实现查找某个页面内容上的效果
    def app_find_ele(self,click_text,page_click_text):
        self.app_click_tab_community()
        self.app_findele_click_channel(click_text)
        self.app_findele_search_page(page_click_text)