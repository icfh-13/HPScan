
import re
from HPScan.module.helper import reader

def get_proxy(path):
    pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
    re_ip = re.compile(pattern)
    text = reader(path, 'r')

    for ip_match in re_ip.findall(text):
        yield ip_match

ip_proxy = get_proxy('E:\PY_code_pro\my_demo\ip_log\Fri Jan  6 23_59_43 2023Ip_Pool.txt')
