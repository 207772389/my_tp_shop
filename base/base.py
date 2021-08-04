from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog

log = GetLog.get_logger()

class Base:

    def __init__(self,driver):
        # 解决driver
        self.driver = driver

    def base_find_element(self,loc,timeout = 30,poll = 0.5):
        '''

        :param loc:需要定位的元素
        :param timeout:查找元素超时时间，默认30秒
        :param poll:查找元素的频率，默认0.5秒
        :return:返回查找到的元素
        '''
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x : x.find_element(*loc))

    def base_input(self,loc,value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    def base_click(self,loc):
        self.base_find_element(loc).click()

    def base_get_text(self,loc):
        return self.base_find_element(loc).text
