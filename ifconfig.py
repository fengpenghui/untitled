#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923


import os
import re
# ifconfig_result = os.open('ifconfig ' + 'ens32').read()
ifconfig_result = 'ens32: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\
              inet 10.1.1.12  netmask 255.255.255.0  broadcast 10.1.1.255\
        inet6 fe80::cd81:9670:2bc7:66b9  prefixlen 64  scopeid 0x20<link>\
        ether 00:0c:29:12:87:8d  txqueuelen 1000  (Ethernet)\
        RX packets 9909  bytes 860148 (839.9 KiB)\
        RX errors 0  dropped 0  overruns 0  frame 0\
        TX packets 2333  bytes 1032404 (1008.2 KiB)\
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0 '
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
