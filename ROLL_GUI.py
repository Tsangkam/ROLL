"""
这个文件用于GUI界面编写
"""

from class_film import Film as film
import tkinter as tk
from tkinter.filedialog import askdirectory
import os
import random


# 检测出文件夹内所有文件
def film_finder(film_list, folder):
    # 路径不存在，返回-1
    if not os.path.exists(folder):
        return -1

    temp_list = os.listdir(folder)

    # 遍历文件夹下所有文件
    for item in temp_list:
        new_folder = folder+'/'+item
        if os.path.isfile(new_folder):     # 如果item是文件，则创建一个film对象并加入list
            movie = film(folder, item)
            if movie not in film_list:
                film_list.append(movie)
            else:
                pass
        elif os.path.isdir(new_folder):    # 如果item是文件夹，则用递归遍历其下所有文件
            film_finder(film_list, new_folder)


# 开启gui界面
def gui_start(folder_list, film_list):
    root = tk.Tk()
    root.title = 'ROLL!'

    # 各类变量设置
    select_dir = tk.StringVar()    # 用于路径选择时的可变参数
    amount = tk.StringVar()
    amount.set(str(len(film_list)))

    # 设置窗口位置
    ww = 400
    wh = 200
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw-ww)/2
    y = (sh-wh)/2
    root.geometry('%dx%d+%d+%d' % (ww, wh, x, y))

    # 各种内置函数
    # 插入按钮回调函数：将选择的目录加入listbox
    def insert():
        folder = en1.get()
        if folder == '':
            return 0
        if folder in folder_list:
            select_dir.set('')
            return 0

        folder_list.append(folder)
        film_finder(film_list, folder)
        listbox.insert(tk.END, folder)
        select_dir.set('')
        amount.set(str(len(film_list)))

    # 从listbox中删除选中的目录及目录下的所有文件
    def remove():
        temp = listbox.get(tk.ACTIVE)

        # 删除film_list中的元素
        for i in range(len(film_list))[::-1]:
            if film_list[i].full_path()[0:len(temp)] == temp:
                del film_list[i]
        folder_list.remove(temp)
        listbox.delete(tk.ACTIVE)
        amount.set(str(len(film_list)))

    # 随机选择一个文件
    def ROLL():
        if not len(film_list) > 0:
            return 0
        a = random.choice(film_list)
        a.start()

    # 各类控件
    tk.Label(root, text='选择文件目录：').place(x=5, y=0)  # 文件夹选择提示标签
    en1 = tk.Entry(root, textvariable=select_dir, width=40)    # 文件目录输入
    en1.place(x=5, y=25)
    tk.Button(root, text='选择',
              command=lambda: select_dir.set(askdirectory())
              ).place(x=300, y=20)   # 选择按钮

    tk.Button(root, text='导入',
              command=insert).place(x=340, y=20)   # 导入按钮
    tk.Button(root, text='移除', command=remove).place(x=300, y=60)
    tk.Button(root, text='ROLL!', command=ROLL).place(x=300, y=100)
    listbox = tk.Listbox(root, width=40)
    tk.Label(root, textvariable=amount).place(x=380, y=180)
    tk.Label(root, text='现有文件数量:').place(x=300, y=180)

    # 初始化listbox
    for item in folder_list:
        listbox.insert(tk.END, item)
    listbox.place(x=5, y=50)

    # 开始消息循环
    root.mainloop()
