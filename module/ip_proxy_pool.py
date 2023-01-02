# coding=utf-8
"""
    To build the IP-Proxy-Pool, we use the python spider techniques based on 're'
"""

import sys, os
sys.path.append(os.getcwd())

# module use
import sys
from time import ctime
import urllib
from urllib import error
from urllib import request
import re
from fake_user_agent import user_agent

from module.helper import writer

# IP代理池的IP源
URLs = {
    '免费代理IP': 'http://ip.yqie.com/ipproxy.htm',  # 1页
    '66免费代理网': 'http://www.66ip.cn/',  # 1.html -> 2919.html
    '89免费代理': 'http://www.89ip.cn/',  # index_1.html -> index_20.html
    '云代理': 'http://www.ip3366.net/',  # http://www.ip3366.net/?stype=1&page=5  (1~10)
    '快代理': 'https://www.kuaidaili.com/free/'  # https://www.kuaidaili.com/free/inha/1/   1~4914
}

# GLOBAL VAR
IP_COUNT = 1000             # 爬取的IP数量设置
IP_INIT_COUNT = 0
FILE_NAME = ctime()

def TestIp(ip):
    """
    检测IP地址是否可以用
    """
    UA = user_agent()
    headers = {
        'User-Agent': UA
    }
    # 使用代理ip进行访问，检测
    req = urllib.request.Request(url="http://www.baidu.com", headers=headers, origin_req_host=ip)
    try:
        page = urllib.request.urlopen(req)
    except:
        return False
    else:
        if page.code == 200:
            return True
        else:
            return False


def Spider(url):
    """
    爬取IP的一般函数
    :param url:
    :return:
    """
    UA = user_agent()
    headers = {
        'User-Agent': UA
    }
    req = urllib.request.Request(url=url, headers=headers)  # 构造请求报文
    try:
        page = urllib.request.urlopen(req)
    except urllib.error.URLError as err_msg:
        if hasattr(err_msg, 'reason'):
            print(f"error reason:{err_msg.reason}")
        elif hasattr(err_msg, 'code'):
            print(f"error code:{err_msg.code}")
    else:
        html = page.read().decode('gbk', 'ignore')              # 获取html资源
        re_ip = r'<td>[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+<\/td>'  # IP正则
        re_port = r'<td>[0-9]{1,5}<\/td>'                       # Port正则
        reobj_ip = re.compile(re_ip)
        reobj_port = re.compile(re_port)
        ip_info = reobj_ip.findall(html)
        port_info = reobj_port.findall(html)
        global IP_INIT_COUNT
        for (i, j) in zip(ip_info, port_info):
            ip_proxy = (i.replace('<td>', '').replace('</td>', '')) + ':' + (j.replace('<td>', '').replace('</td>', ''))
            if TestIp(ip_proxy):
                IP_INIT_COUNT += 1
                if IP_INIT_COUNT > IP_COUNT:
                    exit(1)
                else:
                    writer(filename=f"HPScan/ip_log/{FILE_NAME.replace(':', '_')}Ip_Pool.txt", text=ip_proxy, mode='a')
            else:
                continue


def FetchIp():
    for (site_name, url) in URLs.items():
        if site_name == "免费代理IP":
            Spider(url)
        elif site_name == '66免费代理网':
            for i in range(1, 2920):
                Spider(f"{url}{i}.html")
        elif site_name == '89免费代理':
            for i in range(1, 21):
                Spider(f"{url}index_{i}.html")
        elif site_name == '云代理':
            for i in range(1, 11):
                Spider(f"{url}?stype=1&page={i}")
        elif site_name == '快代理':
            for i in range(1, 4915):
                Spider(f"{url}/inha/{i}")
        else:
            sys.exit(-1)


# def ThraedRunIP():
#     pass


if __name__ == '__main__':
    FetchIp()
