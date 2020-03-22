#!/usr/bin/python3
# coding=utf-8

import os
# p = os.path.pardir
# a = os.path.abspath(os.path.dirname(__file__))
# t = os.path.abspath

# p = os.path.abspath(os.path.join(os.path.dirname('settings.py'),os.path.pardir))
# print(a)
# os.path.pardir是父目录，os.path.abspath是绝对路径

# 举例具体看一下输出：
# print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
# print(os.path.abspath(os.path.dirname(os.getcwd())))
# print(os.path.abspath(os.path.join(os.getcwd(), "..")))
# a = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "analyse_data"))
# print(a)


# a = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir, "moviespider", "comment_data"))
# b = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir, "moviespider", "movie_info_top500.csv"))
# print(b)
# for filename in os.listdir(a):
    # print(filename)
# target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "analyse_data", "wordcloud_pic")
# if not os.path.exists(target_dir):
#         os.mkdir(target_dir)
#         print("所有分析结果保存在 ", target_dir, " 文件夹下...")
base_dir = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir, "moviespider", "comment_data"))
# print(base_dir)
# print("=============")
# # all_files = [base_dir + i for i in os.listdir(base_dir) if os.path.splitext(i)[1] == '.csv']

# for i in os.listdir(base_dir):
#     if os.path.splitext(i)[1] == '.csv':
#         print(os.path.join(base_dir, i))

a = [os.path.join(base_dir, i) for i in os.listdir(base_dir) if os.path.splitext(i)[1] == '.csv']
for x in a:
    print(os.path.basename(x).split('.')[0])
