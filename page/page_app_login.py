import page
from base.app_base import AppBase
from tools.get_log import GetLog

log = GetLog.get_logger()
from time import sleep

class PageAppLogin(AppBase):

    # 打开app，点击 注册/登录 入口
    def applogin_click_login_enter(self):
        sleep(1)
        self.base_click(page.app_login_enter_btn)

    # 进入输入手机号页面
    def applogin_input_phone_num(self, phone):
        self.base_input(page.app_login_input_phone_num, phone)

    # 点击同意隐私协议选项
    def applogin_agree_check(self):
        self.base_click(page.app_login_agree_check)

    # 点击完同意隐私协议后 点击下一步
    def applogin_click_next_btn(self):
        self.base_click(page.app_login_next_btn)

    # 进入输入登录密码页面
    def applogin_input_pwd(self, pwd):
        self.base_input(page.app_login_input_pwd, pwd)

    # 点击登录按钮
    def applogin_click_login_btn(self):
        self.base_click(page.app_login_btn)

    # 登录成功后 进入首页 获取顶部“首页”文案》供断言调用，判断登录成功
    def applogin_homepage_get_text(self):
        return self.base_get_text(page.app_login_success,2)

    # 把登录过程 业务组合下
    def applogin_login_app(self, phone, pwd):
        log.info("开始调用app登录了，登录用户名是：{}，密码是：{}".format(phone,pwd))
        self.applogin_click_login_enter()
        self.applogin_input_phone_num(phone)
        self.applogin_agree_check()
        self.applogin_click_next_btn()
        self.applogin_input_pwd(pwd)
        self.applogin_click_login_btn()
        self.applogin_homepage_get_text()


