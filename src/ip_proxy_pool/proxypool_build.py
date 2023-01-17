# coding=utf-8
"""
    To build the IP-Proxy-Pool, we use the python spider techniques based on 're'
"""

# add to the root path
import os
import sys
sys.path.append(f"{os.path.dirname(__file__)}")


# module
from time import ctime
from spider import spider

# GLOBAL VAR
URLs = {
    '免费代理IP': 'http://ip.yqie.com/ipproxy.htm',  
    '66免费代理网': 'http://www.66ip.cn/',  
    '89免费代理': 'http://www.89ip.cn/',  
    '云代理': 'http://www.ip3366.net/',  
    '快代理': 'https://www.kuaidaili.com/free/'  
}
IP_COUNT = 3000                         # 爬取的IP数量设置
TEST_URL = "http://www.baidu.com"       # 测试网站
FILE_NAME = ctime()                     # ip日志生成文件名


def fetch_ip():
    for (site_name, url) in URLs.items():
        if site_name == "免费代理IP":
            spider(url=url, test_url=TEST_URL, ip_count=IP_COUNT, filename=FILE_NAME)
        elif site_name == '66免费代理网':
            for i in range(1, 2920):
                spider(url=f"{url}{i}.html", test_url=TEST_URL, ip_count=IP_COUNT, filename=FILE_NAME)
        elif site_name == '89免费代理':
            for i in range(1, 21):
                spider(url=f"{url}index_{i}.html", test_url=TEST_URL, ip_count=IP_COUNT, filename=FILE_NAME)
        elif site_name == '云代理':
            for i in range(1, 11):
                spider(url=f"{url}?stype=1&page={i}", test_url=TEST_URL, ip_count=IP_COUNT, filename=FILE_NAME)
        elif site_name == '快代理':
            for i in range(1, 4915):
                spider(url=f"{url}/inha/{i}", test_url=TEST_URL, ip_count=IP_COUNT, filename=FILE_NAME)
        else:
            print(f"{os.getcwd()}:Can't find the IP Source!")
            exit(-1)

fetch_ip()
