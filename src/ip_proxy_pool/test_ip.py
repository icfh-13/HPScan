"""
    check if an IP is usable
"""


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
