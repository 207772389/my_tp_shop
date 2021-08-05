from selenium.webdriver.support.wait import WebDriverWait

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
        return self.base_find_element(loc,eles = ele).text
