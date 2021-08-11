from selenium.webdriver.common.by import By

from base.base import Base
from selenium.common.exceptions import NoSuchElementException

class AppBase(Base):
    #查找页面是否存在指定元素
    def app_base_is_exist(self,loc):
        try:
            #调用查找方法
            #这里记得把timeout改为3，默认的30秒超时时间太久了，只是查看页面上是否有元素，两三秒就够用了
            self.base_find_element(loc,timeout=3)
            #输出信息
            print("找到{}元素啦".format(loc))
            #返回True
            return True
        except:
            #输出信息
            print("没有找到{}元素！".format(loc))
            #返回False
            return False

    #封装从右向左滑动方法
    def app_base_right_wipe_left(self,loc_area,click_text):
        """

        :param loc_area: 需要滑动的区域
        :param click_text: 滑动区域里需要点击的元素
        :return:
        """
        #查找区域元素
        el = self.base_find_element(loc_area)
        #获取区域元素的位置 y坐标
        y = el.location.get("y")
        #获取区域元素的宽高
        width = el.size.get("width")
        height = el.size.get("height")
        #计算start_x,start_y,end_x,end_y
        start_x = width*0.8
        start_y = y+height*0.5
        end_x=width*0.2
        end_y = start_y
        loc = By.XPATH,"//*[contains(@text,'{}')]".format(click_text)
        #循环操作 循环滑动查找区域 来寻找区域内要点击的元素
        while True:
            #获取当前屏幕页面结构 每次滑动的时候 需要判断是否为最后一页
            page_source = self.driver.page_source
            #查找元素 找不到的时候就会报错，所以这里加上try
            try:
                #查找元素时 记得修改等待时间
                el = self.base_find_element(loc,timeout=3)
                #如果没有报错 就说明找到了
                #输出提示信息
                print("找到{}元素啦！".format(loc))
                #找到元素后并点击，同时跳出循环了
                el.click()
                break
            except:
                #没有找到元素
                print("未找到{}元素".format(loc))
                #滑动屏幕 继续寻找
                self.driver.swipe(start_y,start_y,end_x,end_y,duration=2000)
            #判断是否为最后一页 重新获取一次页面结果 和上次的比对来判断是否为最后一页
            if page_source == self.driver.page_source:
                #如果是最后一页 上面的break也没有执行 就说明滑动到最后时也没有找到
                print("滑动找了一遍，还是没有找到{}元素".format(loc))
                #抛异常
                raise NoSuchElementException