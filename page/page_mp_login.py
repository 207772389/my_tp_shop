from base.base import Base


class PageMpLogin(Base):

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