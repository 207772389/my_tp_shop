from base.base import Base
import page
from time import sleep

class PageMpLogin(Base):

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
        print("测试下push地址")