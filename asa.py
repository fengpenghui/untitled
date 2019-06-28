#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923

import re

asa_conn = "TCP Student  192.168.189.167:32806 Teacher  137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n \
TCP Student  192.168.189.167:80 Teacher  137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO "

asa_dict = { }

list = str.split('\n')  # 将字符串转化为list

#print(list)

for conn in asa_conn.split('\n'):
    re_result = re.match('.*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                   ':(\d{1,5}).*(bytes\s*\d+).*(flags\s*[A-Z]*)',conn).groups()
    re_result_key = re_result[0],re_result[1],re_result[2],re_result[3]
    re_result_v = re_result[4],re_result[5]
    dict[re_result_key] = re_result_v

print("打印字典\n")

print(asa_dict)
# print('\n')
#
#
# print("格式化打印输出\n")
# for key,value in dict.items():
#
#     print('src:{0:<20s}|src_p:{1:<20s}|dst:{2:<20s}|dst_p:{3:<20s}'.format(key[0],key[1],key[2],key[3]))
#     print('byes:{0:<19s}|flags:{1:<20s}'.format(value[0],value[1]))
#     print('=' * 110)
# #采用了新的.format的方法对齐