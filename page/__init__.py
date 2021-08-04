from selenium.webdriver.common.by import By

"""以下数据为黑马头条登录页面配置数据"""
# 13812345678 246810
# 用户名
mp_username = (By.CSS_SELECTOR,"[placeholder='用户名']")
# 密码
mp_pwd = (By.CSS_SELECTOR,"[placeholder='密码']")
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR,".ant-btn")
# 登录后页面右上角的昵称
mp_nickname = (By.CSS_SELECTOR,".antd-pro-components-global-header-index-name")

"""以下为登录的url"""
admin_url = "http://promoting-admin.picooc.com/#/user/login"
