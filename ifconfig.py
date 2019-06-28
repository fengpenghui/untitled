#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923


import os
import re
ifconfig_result = os.popen('ifconfig ' + 'ens32').read()
#正则表达式查找IP，掩码，广播和mac地址
ipv4_addr = re.findall('inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+',ifconfig_result)[0]
netmask = re.findall('netmask\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+',ifconfig_result)[0]
broadcast = re.findall('broadcast\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+',ifconfig_result)[0]
mac_addr = re.findall('ether\s+(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})\s+',ifconfig_result)[0]
#格式化字符串
format_string = '{0:<10s}:{1:<20s}'
#打印结果
print(format_string.format('ipv4_addr',ipv4_addr))
print(format_string.format('netmask',netmask))
print(format_string.format('broadcast',broadcast))
print(format_string.format('mac_addr',mac_addr))

#产生网关的IP地址
ipv4_gw = ipv4_addr.split('.')
ipv4_gw[3] = '254'
ipv4_gw = '.'.join(ipv4_gw)

#打印网关的IP地址
print('\n我们假设网关地址为最后一位为254，因此网关IP地址为：' + ipv4_gw + '\n')

#ping网关
ping_result = os.popen('ping '+ ipv4_gw + ' -c 1').read().replace('\n',' ')
re_ping_result = re.findall('(ttl|TTL)=',ping_result)
if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达！')
