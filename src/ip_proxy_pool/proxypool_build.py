# coding=utf-8
"""
    To build the IP-Proxy-Pool, we use the python spider techniques based on 're'
"""
# add to the root path
import os
import sys
from time import ctime

sys.path.append(os.getcwd())


from spider import spider

# GLOBAL VAR
URLs = {
    '免费代理IP': 'http://ip.yqie.com/ipproxy.htm',  # 1页
    '66免费代理网': 'http://www.66ip.cn/',  # 1.html -> 2919.html
    '89免费代理': 'http://www.89ip.cn/',  # index_1.html -> index_20.html
    '云代理': 'http://www.ip3366.net/',  # http://www.ip3366.net/?stype=1&page=5  (1~10)
    '快代理': 'https://www.kuaidaili.com/free/'  # https://www.kuaidaili.com/free/inha/1/   1~4914
}
IP_COUNT = 1000  # 爬取的IP数量设置
TEST_URL = "http://www.baidu.com"
FILE_NAME = ctime()

def FetchIp():
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
            sys.exit(-1)


# def ThraedRunIP():
#     pass


if __name__ == '__main__':
    FetchIp()
