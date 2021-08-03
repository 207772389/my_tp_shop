# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/3 19:34
@Auth ： cainiao
@File ：get_log.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import logging.handlers
import os

from config import BASE_PATH



class GetLog:
    #新建一个日志器变量，和获取driver思路类似，单利模式
    #不让外界通过类名.调用
    __logger = None

    #弄成类方法方便类名.调用
    @classmethod
    def get_logger(cls):
        if cls.__logger is None:
            #获取日志器
            cls.__logger = logging.getLogger()
            #修改日志器默认级别
            cls.__logger.setLevel(logging.INFO)
            #获取处理器 这里使用时间切片处理器\
            log_path = BASE_PATH + os.sep +"log"+os.sep+"picooc.log"
            th = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s : %(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            #将格式器添加到处理器中
            th.setFormatter(fm)
            #将处理器添加到日志器中
            cls.__logger.addHandler(th)
        return cls.__logger

if __name__ == '__main__':
    log = GetLog.get_logger()
    log.info("测试信息级别")
    log.error("错误级别日志")
