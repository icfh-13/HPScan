import re
from file_handler import reader


def get_proxy_ip(path):
    pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
    re_ip = re.compile(pattern)
    text = reader(path, 'r')
    for ip_match in re_ip.findall(text):
        yield ip_match
