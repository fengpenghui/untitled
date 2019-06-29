#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923

import os

os.mkdir('test')
os.chdir('test')
qytang1 = open('qytang1','w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()
qytang2 = open('qytang2','w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3','w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
os.mkdir('qytang4')
os.mkdir('qytang5')

path = '/tmp/pycharm_project_377/test'

tasks_floder = os.listdir('/tmp/pycharm_project_377/test')

s = []

for x in tasks_floder:
    f = path + "/" + x  # f是绝对路径
    if os.path.isdir(f):  # 如果是目录则跳过
        pass
    else:
        for line in open(f).readlines():  # 逐行读取f，并迭代到line中
            if 'qytang' in line:  # 判断文件中是否包含字符
                s.append(x)  # 符合条件的添加进空列表

print("文件中包含'qytang'关键字的文件为:")
print("\n".join(s))