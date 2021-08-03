from selenium.webdriver.common.by import By

from base.base import Base
from time import sleep

class WebBase(Base):
    """以下为web项目专属方法"""
    #根据placeholder文本点击指定元素
    def web_base_click_element(self,placeholder_text,click_text):
        #点击父选框
        loc = By.CSS_SELECTOR,"[placeholder='{}']".format(placeholder_text)
        self.base_click(loc)
        #暂停一秒，父选框弹出下拉列表需要时间
        sleep(1)
        #在弹出的列表上点击包含要点击文本的元素
        loc = By.XPATH,"//*[text()='{}']".format(click_text)
        self.base_click(loc)