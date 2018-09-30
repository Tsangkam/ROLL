"""
ROLL! 功能介绍
1.用户选择文件夹并导入其中所有文件
2.在用户导入得所有文件中选择一个随机文件并用默认打开方式打开
3.记录文件打开次数
4.记录历史打开文件
5.修复了此前存在的空列表时依然可以打开文件的bug
"""


from ROLL_GUI import *
from config import *
import csv


# 全局变量
folder_list = []   # 用于保存用户选择的文件夹
film_list = []     # 用于保存用户选择的所有文件


# 用于读取之前导入的路径及电影名
def read_list():
    if not os.path.exists(r'data'):
        os.mkdir(r'data')
        f = open(list_path, 'w')
        f.close()
        f = open(history_path, 'w')
        f.close()
        f = open(film_data, 'w')
        f.close()
    with open(list_path, 'r') as f:
        for item in f.readlines():
            if item != '\n':
                folder_list.append(item[0:-1])

    with open(film_data, 'r') as f:
        c_file = csv.reader(f)
        for item in c_file:
            a = film(item[1], item[0], eval(item[2]))
            film_list.append(a)


# 用于保存数据
def save_list():
    # 保存列表数据
    with open(list_path, 'w') as f:
        for item in folder_list:
            f.writelines(item+'\n')

    # 保存文件数据
    with open(film_data, 'w') as f:
        for it in film_list:
            f.writelines(it.name() + ',' + it.father_path() + ',' + str(it.display_times()) + '\n')


# 主函数
def main():
    read_list()
    gui_start(folder_list, film_list)
    save_list()


main()
