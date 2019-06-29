#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923

import re

str = """TCP Student  192.168.189.167:32806 Teacher  137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO 
TCP Student  192.168.189.167:80 Teacher  137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO """

dict = {}

list = str.split('\n')

for i in list:

    res = re.match('.*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                   ':(\d{1,5}).*(bytes\s*\d+).*(flags\s*[A-Z]*)',i).groups()
    res_key = res[0],res[1],res[2],res[3]
    res_v = res[4],res[5]
    dict[res_key] = res_v

print("打印字典\n")

print(dict)
print('\n')


print("格式化打印输出\n")
for key,value in dict.items():

    print(' src:{0:<20s}|src_p:{1:<19s}|dst:{2:<20s}|dst_p:{3:<20s}'.format(key[0],key[1],key[2],key[3]))
    print('byes:{0:<19s} |flags:{1:<20s}'.format(value[0],value[1]))
    print('=' * 110)