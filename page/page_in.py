from page.page_add_pd import PageAddPd
from page.page_mp_login import PageMpLogin
# TODO 现在还不太明白为什么要加这个统一入口类，我理解要用这个类的实例时直接 类() 然后赋值到一个变量上即可，不是吗？

class PageIn:

    def __init__(self,driver):
        self.driver = driver

    #登录页面
    def pagein_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    #添加商品页面
    def pagein_get_PageAddPd(self):
        return PageAddPd(self.driver)