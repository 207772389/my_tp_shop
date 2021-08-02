from selenium.webdriver.common.by import By

"""以下数据为黑马头条登录页面配置数据"""
# 13812345678 246810
# 用户名
mp_username = (By.CSS_SELECTOR,"[placeholder='请输入手机号']")
# 验证码
mp_code = (By.CSS_SELECTOR,"[placeholder='验证码']")
# 登录按钮
mp_code = (By.CSS_SELECTOR,".el-button--primary")
# 昵称