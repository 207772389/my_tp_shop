from selenium.webdriver.common.by import By

"""以下数据为黑马头条登录页面配置数据"""
# 13812345678 246810
# 用户名
mp_username = (By.CSS_SELECTOR, "[placeholder='用户名']")
# 密码
mp_pwd = (By.CSS_SELECTOR, "[placeholder='密码']")
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR, ".ant-btn")
# 登录后页面右上角的昵称
mp_nickname = (By.CSS_SELECTOR, ".antd-pro-components-global-header-index-name")

"""以下为后台登录的url"""
admin_url = "http://promoting-admin.picooc.com/#/user/login"

"""以下为商品列表页面的配置数据"""
# 新建
pd_list_add_btn = (By.XPATH, "//*[text()='新建']/parent::button")
# 状态
pd_list_status = (By.CSS_SELECTOR, "#status")
#点击状态后 下拉列表里选择编辑中，注意：这里返回的是元素列表，选择第一个即可
pd_list_choose_status = (By.CSS_SELECTOR,".ant-table-filter-dropdown>ul>li:nth-child(1)")
#商品名称：注意：这里是返回了元素列表，要取第二个元素
pd_list_pd_name = (By.CSS_SELECTOR,".ant-table-tbody>tr>td")
#提交审批按钮,注意：这里返回的是元素列表，取第一个值即可
pd_list_sumit_sp=(By.XPATH,"//*[text()='提交审批']")
#查询按钮
pd_list_search_btn = (By.XPATH,"//*[text()='查 询']")


"""以下为新增商品页面的配置元素"""

# 商品标题，这里注意下：通过这个能定位到两个元素，到时候直接取第一个就行
pd_adding_pd_title = (By.CSS_SELECTOR, "[placeholder='不超过30字']")
# 商品名称，这里注意下：通过这个能定位到两个元素，到时候直接取第二个就行
pd_adding_pd_name = (By.CSS_SELECTOR, "[placeholder='不超过30字']")
# 商品类型
pd_adding_pd_type = (By.CSS_SELECTOR, "#type")
# 服务类
pd_adding_pd_typevalue = (By.XPATH, "//*[text()='服务类']")
# 预热时间》点击开始日期
pd_adding_click_data = (By.CSS_SELECTOR, "[placeholder = '开始日期']")
# 预热时间》开始日期
pd_adding_start_data = (By.CSS_SELECTOR, ".ant-calendar-today>div")
# 预热时间》结束日期
pd_adding_end_data = (By.CSS_SELECTOR, ".ant-calendar-today+td>div")
# 选完预热日期后的确定按钮
pd_adding_date_ok = (By.CSS_SELECTOR, ".ant-calendar-ok-btn")
# 用户评价
pd_adding_evluation = (By.XPATH, "//*[text()='燃脂营评价']")
# 分享标题
pd_adding_share_title = (By.CSS_SELECTOR, "#shareTitle")
# 分享描述
pd_adding_share_info = (By.CSS_SELECTOR, "#shareInfo")
# 保存按钮
pd_adding_save_btn = (By.XPATH, "//*[text()='保 存']/parent::button")
#确认保存的弹框上的确认按钮
pd_adding_makesure_ok = (By.XPATH,"//*[text()='确 认']/parent::button")

