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
admin_url = "http://172.17.0.20:9094/#/user/login"
# admin_url = "http://promoting-admin.picooc.com/#/user/login"

"""以下为商品列表页面的配置数据"""
# 新建
pd_list_add_btn = (By.XPATH, "//*[text()='新建']/parent::button")
# 状态
pd_list_status = (By.CSS_SELECTOR, "#status")
# 点击状态后 下拉列表里选择编辑中，注意：这里返回的是元素列表，选择第一个即可
pd_list_choose_status = (By.CSS_SELECTOR, ".ant-table-filter-dropdown>ul>li:nth-child(1)")
# 商品名称：注意：这里是返回了元素列表，要取第二个元素
pd_list_pd_name = (By.CSS_SELECTOR, ".ant-table-tbody>tr>td")
# 提交审批按钮,注意：这里返回的是元素列表，取第一个值即可
pd_list_submit_sp = (By.LINK_TEXT, "提交审批")
#提交审批后 点击通过 按钮，注意：取第一个元素
pd_list_click_pass=(By.LINK_TEXT,"通过")
#通过后 点击 上架按钮，注意：取第一个元素
pd_list_click_sj=(By.LINK_TEXT,"上架")
# 查询按钮
pd_list_search_btn = (By.XPATH, "//*[text()='查 询']")
# 商品成功上架后，获取商品的状态
pd_list_get_pd_status = (By.XPATH,"//*[text()='已上架']")

"""以下为新建sku的配置元素"""
# sku管理,注意：这里返回的是元素列表，取第二个元素
pd_list_sku_manage = (By.CSS_SELECTOR, ".ant-table-tbody> tr:nth-child(1) > td:nth-child(7) > a")
# 新建sku
pd_list_add_sku = (By.XPATH, "//*[text()='新建sku']/parent::button")
# 新增sku
pd_list_addsku_btn = (By.XPATH, "//*[text()='新增SKU']/parent::button")
# 新增sku页面 输入周期
pd_list_addsku_period = (By.XPATH, "//*[@id='period']")
# sku名称
pd_list_addsku_skuname = (By.CSS_SELECTOR, "#name")
# 新增sku页面 开营时间，注意：这里返回的是元素列表，记得取第一个值
pd_list_addsku_starttime_btn = (By.CSS_SELECTOR, "[placeholder='请选择日期']")
#选择今天
pd_list_addsk_choose_starttime = (By.CSS_SELECTOR,".ant-calendar-today>div")
# 选择好开营时间的确定按钮
pd_list_addsku_starttime_ok = (By.CSS_SELECTOR, ".ant-calendar-ok-btn")
# 原价
pd_list_addsku_originprice = (By.CSS_SELECTOR, "#originPrice")
# 现价
# pd_list_addsku_currentprice = (By.CSS_SELECTOR, "#curentPrice")
# 特价
pd_list_addsku_especialprice = (By.CSS_SELECTOR, "#especialPrice")
# 保存按钮
pd_list_addsku_first_savebtn = (By.PARTIAL_LINK_TEXT, "保存")
# 底部的保存按钮
pd_list_addsku_second_savebtn = (By.XPATH, "//*[text()='保 存']/parent::button")

#sku保存后 返回到sku列表 点击提交审批
pd_list_addsku_skulist_sp =(By.PARTIAL_LINK_TEXT,"提交审批")
#sku审批通过
pd_list_addsku_skulist_pass_sp =(By.PARTIAL_LINK_TEXT,"通过审批")
#sku点击上架 至此，sku上架通过了，去商品列表里提交商品到上架状态
pd_list_addsku_skulist_sj =(By.LINK_TEXT,"上架")

#点击左边列表里的 商品列表
pd_list_click_pdlist =(By.XPATH,"//*[text()='商品列表']/parent::a")


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
# 确认保存的弹框上的确认按钮
pd_adding_makesure_ok = (By.XPATH, "//*[text()='确 认']/parent::button")

"""以下信息为APP登录相关的配置信息"""
#app的包名
appPackage = "com.picooc"
#app的启动页
appActivity="com.picooc.activity.start.WelcomeActivity"
#注册登录按钮
app_login_enter_btn = (By.ID,"com.picooc:id/login_text")
#输入手机号
app_login_input_phone_num = (By.ID,"com.picooc:id/phone_register")
#同意隐私协议选项
app_login_agree_check=(By.ID,"com.picooc:id/agree_selector")
#输入手机号后 点击下一步
app_login_next_btn = (By.ID,"com.picooc:id/btn_get_identifying_code_register")
#输入登录密码
app_login_input_pwd=(By.ID,"com.picooc:id/pwd")
#登录按钮
app_login_btn=(By.ID,"com.picooc:id/btn_login")
#进入首页后 通过获取页面顶部的 首页 文案，来判断登录成功了。注意：这里返回的是元素列表，记得取第一个即可
app_login_success=(By.ID,"com.picooc:id/tv_tab_name")

#滑动区域
app_channel_area = By.XPATH,"//*[@class='android.widget.HorizontalScrollView']"