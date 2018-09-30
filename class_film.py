"""
此文件内为电影类声明
"""


import win32api
from config import *
import datetime


# 电影类
class Film:
    __name = str()  # 电影名
    __path = str()  # 电影文件路径
    __times = 0  # 电影打开次数

    # 初始化电影类
    def __init__(self, path, name, times=0):
        self.__name = name
        self.__path = path
        self.__times = times

    # 以默认打开方式打开
    def start(self):
        self.__times = self.__times + 1
        with open(history_path, 'a') as f:
            f.writelines(self.name() + ',' + self.full_path() + ',' +
                         datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        win32api.ShellExecute(0, 'open', self.full_path(), '', '', 1)

    # 查看电影名
    def name(self):
        return self.__name

    # 查看电影父路径
    def father_path(self):
        return self.__path

    # 查看电影全路径
    def full_path(self):
        return self.__path+'/'+self.__name

    # 查看播放次数
    def display_times(self):
        return self.__times
