"""
此文件内为电影类声明
"""


import win32api


# 电影类
class Film:
    __name = 'empty'  # 电影名
    __path = 'empty'  # 电影文件路径
    __times = 0  # 电影打开次数

    # 初始化电影类
    def __init__(self, path, name):
        self.__name = name
        self.__path = path

    # 以默认打开方式打开
    def start(self):
        self.__times = self.__times + 1
        win32api.ShellExecute(0, 'open', self.__path, '', '', 1)

    # 查看电影名
    def name(self):
        return self.__name

    # 查看电影路径
    def path(self):
        return self.__path

    # 查看电影打开次数
    def times(self):
        return self.__times
