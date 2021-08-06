from base.base import Base


class AppBase(Base):
    #查找页面是否存在指定元素
    def app_base_is_exist(self,loc):
        try:
            #调用查找方法
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