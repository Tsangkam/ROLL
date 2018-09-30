"""
ROLL! 功能介绍
1.用户选择文件夹并导入其中所有文件
2.在用户导入得所有文件中选择一个随机文件并用默认打开方式打开
3.记录文件打开次数
4.记录历史打开文件
"""

from class_film import Film as film
import random
import os
from ROLL_GUI import *


counter = 0
max_display = 0
list_path = r'data/list.txt'
history_path = r'data/history.txt'


# 用于读取之前导入的路径及电影名
def read_list():
    if not os.path.exists(list_path) or not os.path.exists(history_path):
        os.mkdir(r'data')
        f = open(list_path, 'w')
        f.close()
        f = open(history_path, 'w')
        f.close()


# 用于
def save_list():
    pass


# 主函数
def main():
    read_list()
    gui_start()
    save_list()


main()
