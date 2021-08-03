from base.web_base import WebBase


class PageMpLogin(WebBase):

    def pagelogin_input_username(self):
        pass

    def pagelogin_input_pwd(self):
        pass

    def pagelogin_click_login_btn(self):
        pass

    def pagelogin_get_nickname(self):
        pass

    def pagelogin_mp_login(self,username,pwd):
        self.pagelogin_input_username(username)
        self.pagelogin_input_pwd(pwd)
        self.pagelogin_click_login_btn()

    #组合业务方法》发布文章前调用，登录进去
    def pagelogin_mp_login(self, username="shangqianchen", pwd="picooc_123"):
        self.pagelogin_input_username(username)
        self.pagelogin_input_code(pwd)
        self.pagelogin_click_login_btn()