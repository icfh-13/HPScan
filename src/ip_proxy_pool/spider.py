"""
    
"""
# add to the root path
import sys
import os
sys.path.append(os.path.dirname(__file__))  # ..\HPScan\src\ip_proxy_pool            
sys.path.append(f"{os.path.dirname(__file__)}\\..\\")   # ..\HPScan\src
sys.path.append(f"{os.path.dirname(__file__)}\\..\\..\\")   # ..\HPScan 

# module
import time
import urllib
import re
from fake_user_agent import user_agent
from urllib import request
from urllib import error

from test_ip import test_ip
from helper.file_handler import writer

IP_INIT_COUNT = 0
IP_LOG_PATH_FOR_SPIDER = f"{os.path.dirname(__file__)}\..\..\log\ip_log"


def spider(url, test_url, ip_count, filename):
    UA = user_agent()
    headers = {
        'User-Agent': UA
    }
    req = urllib.request.Request(url=url, headers=headers)
    try:
        page = urllib.request.urlopen(req)
        time.sleep(0.05)
    except urllib.error.URLError as err_msg:
        if hasattr(err_msg, 'reason'):
            print(f"error reason:{err_msg.reason}")
        elif hasattr(err_msg, 'code'):
            print(f"error code:{err_msg.code}")
    except Exception as err_msg:
        print(f"error msg:{err_msg}")
    else:
        html = page.read().decode('gbk', 'ignore')
        pattern_ip = r'<td>[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+<\/td>'
        pattern_port = r'<td>[0-9]{1,5}<\/td>'
        re_ip = re.compile(pattern_ip)
        re_port = re.compile(pattern_port)
        ip_info = re_ip.findall(html)
        port_info = re_port.findall(html)
        global IP_INIT_COUNT
        for (i, j) in zip(ip_info, port_info):
            ip_proxy = (i.replace('<td>', '').replace('</td>', '')) + ':' + (j.replace('<td>', '').replace('</td>', ''))
            if test_ip(ip_proxy, test_url):
                IP_INIT_COUNT += 1
                if IP_INIT_COUNT > ip_count:
                    exit(1)
                else:
                    # path:../HPScan/log/ip_log/
                    writer(path=f"{IP_LOG_PATH_FOR_SPIDER}\{filename.replace(':', '_').replace(' ', '_')}_IP_Pool.txt",
                           text=ip_proxy, mode='a')
            else:
                continue

