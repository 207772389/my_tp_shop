from time import sleep

import page
from base.web_base import WebBase


class PageMpLogin(WebBase):

    def pagelogin_input_username(self,username):
        self.base_input(page.mp_username,username)

    def pagelogin_input_pwd(self,pwd):
        self.base_input(page.mp_pwd,pwd)

    def pagelogin_click_login_btn(self):
        sleep(1)
        self.base_click(page.mp_login_btn)

    #断言的时候调用
    def pagelogin_get_nickname(self):
        return self.base_get_text(page.mp_nickname)
    #组合业务方法》测试脚本里调用
    def pagelogin_mp_login(self,username,pwd):
        self.pagelogin_input_username(username)
        self.pagelogin_input_pwd(pwd)
        self.pagelogin_click_login_btn()

    #组合业务方法》发布文章依赖调用
    def pagelogin_mp_login_sucess(self,username="shangqianchen",pwd="picooc_123"):
        self.pagelogin_input_username(username)
        self.pagelogin_input_pwd(pwd)
        self.pagelogin_click_login_btn()