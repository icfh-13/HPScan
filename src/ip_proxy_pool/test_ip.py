"""
    check if an IP is usable
"""
# add to the root path
import sys
import os
sys.path.append(os.path.dirname(__file__))  # ..\HPScan\src\ip_proxy_pool            
sys.path.append(f"{os.path.dirname(__file__)}\\..\\")   # ..\HPScan\src
sys.path.append(f"{os.path.dirname(__file__)}\\..\\..\\")   # ..\HPScan s

# module
import urllib
from urllib import request
from urllib import error
from fake_user_agent import user_agent

def test_ip(ip, test_url):
    UA = user_agent()
    headers = {
        'User-Agent': UA
    }
    req = urllib.request.Request(url=test_url, headers=headers, origin_req_host=ip)
    try:
        page = urllib.request.urlopen(req)
    except urllib.error as msg_err:
        print(f"Sorry,{msg_err}")
        return False
    else:
        if page.code == 200:
            return True
        else:
            return False
