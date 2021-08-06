from page.page_in import PageIn
from tools.get_driver import GetDriver
from time import sleep

from tools.get_log import GetLog

log = GetLog.get_logger()

class TestAppLogin():

    #初始化
    def setup_class(self):
        #获取driver
        driver = GetDriver.get_app_driver()
        #通过统一入口类获取applogin对象
        self.app_login = PageIn(driver).pagein_get_PageAppLogin()

    #销毁
    def teardown_class(self):
        sleep(5)
        GetDriver.quit_app_driver()
    #测试业务方法
    def test_app_login(self):
        self.app_login.applogin_login_app("17611240359","a1234567")
        try:
            assert "首页"==self.app_login.applogin_homepage_get_text()
        except Exception as e:
            #截图
            self.app_login.base_get_screen_shot()
            #日志
            log.error("登录失败了，失败原因是：{}".format(e))
            #抛异常
            raise