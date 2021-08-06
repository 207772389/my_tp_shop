import os
import time

import allure
from selenium.webdriver.support.wait import WebDriverWait

from config import BASE_PATH
from tools.get_log import GetLog

log = GetLog.get_logger()

class Base:

    def __init__(self,driver):
        # 解决driver
        self.driver = driver

    # def base_find_element(self,loc,timeout = 30,poll = 0.5):
    #     '''
    #
    #     :param loc:需要定位的元素
    #     :param timeout:查找元素超时时间，默认30秒
    #     :param poll:查找元素的频率，默认0.5秒
    #     :return:返回查找到的元素
    #     '''
    #     log.info("正在查找元素：{}".format(loc))
    #     return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x : x.find_element(*loc))

    def base_find_element(self,loc,timeout = 30,poll = 0.5,eles = 1):
        '''

        :param loc: 需要定位的元素
        :param timeout: 查找元素超时时间，默认30秒
        :param poll: 查找元素的频率，默认0.5秒
        :param eles: 这个参数是为了控制是使用find_element还是使用find_elements，因为有的元素定位后会返回来多个，
                        通过find_elements返回后取第一个或者第二个值，比如page_add_pd页面的商品标题和商品名称
        :return:
        '''
        log.info("正在查找元素：{}".format(loc))
        if eles ==1:
            return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x : x.find_element(*loc))
        elif eles ==2:
            log.info("根据：{}找到了多个元素".format(loc))
            return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x : x.find_elements(*loc))[0]
        else:
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))[1]

    def base_input(self,loc,value,ele = 1):
        el = self.base_find_element(loc,eles=ele)
        el.clear()
        el.send_keys(value)

    def base_click(self,loc,ele = 1):
        self.base_find_element(loc,eles = ele).click()

    def base_get_text(self,loc,ele = 1):
        log.info("正在获取元素:{}的text，值为：{}".format(loc,self.base_find_element(loc,eles = ele).text))
        return self.base_find_element(loc,eles = ele).text

    def base_get_screen_shot(self):
        #调用截图方法
        log.error("断言出错啦，开始截图了！！！")
        self.img_path = BASE_PATH + os.sep+"image"+os.sep+"error_img_{}.png".format(time.strftime("%Y-%m-%d %H-%M-%S"))
        self.driver.get_screenshot_as_file(self.img_path)
        #调用下面的图片写入报告方法

    #这里为了避免外部调用 这几搞成了私有方法
    def __base_write_imge(self):
        # 获取图片文件流
        with open(self.img_path,"rb") as f:
            #调用allure.attach附加方法
            allure.attach("错误原因：",f.read(),allure.attachment_type.PNG)
