#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923


import os
import re
route_n_result = os.popen("route -n").read()  #执行并返回命令的结果
ipv4_gw =  re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+UG',route_n_result)[0]
print('网关为：'+str(ipv4_gw))