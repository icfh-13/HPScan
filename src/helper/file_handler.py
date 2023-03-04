"""
    THE FUNCTIONS BELOW HELP TO HANDLER THE I/O_STREAM OF FILE
"""

# module use
import sys
import re

def reader(path, mode='r'):
    try:
        with open(file=path, mode=mode) as f:
            text = f.read()
        return text
    except:
        print("file read error!")
        exit(-1)


def writer(path, text, mode):
    try:
        if 'b' in mode:
            with open(file=path, mode=mode) as f:
                f.write(text)
                f.write('\n')
        else:
            with open(file=path, mode=mode, encoding='utf-8') as f:
                f.write(text)
                f.write('\n')
    except:
        print("file write error!")
        sys.exit(-1)
import re


def get_proxy_ip(path):
    """read ip from the ip_log file"""
    pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
    re_ip = re.compile(pattern)
    text = reader(path, 'r')
    for ip_match in re_ip.findall(text):
        yield ip_match


def get_proxy_port(path):
    """read port from the ip_log file"""
    pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:([0-9]*)'
    re_port = re.compile(pattern)
    text = reader(path, 'r')
    for port_match in re_port.findall(text):
        yield port_match

