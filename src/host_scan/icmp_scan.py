# coding=utf-8
"""
    based on ICMP protocol
"""

import sys
import os
sys.path.append(os.getcwd())

# src use

from scapy.layers.inet import *
from scapy.layers.l2 import *
from scapy.all import *

from HPScan.src.helper.read_proxy_ip import get_proxy_ip


def icmp_scan(dst_ip, proxy_path):
    """ICMP SCAN"""
    try:
        src_ip = get_proxy_ip(proxy_path)
        pkt = Ether() / IP(src=src_ip, dst=dst_ip) / ICMP(type=8) / b'hello?'  # 构造数据包
        req = srp1(pkt, timeout=2, verbose=False)
        if req:
            print(f'[+]{dst_ip}:Host is up')
            self.alive_hosts.append(dst_ip)
            self.count += 1
        else:
            print(f'[-]{dst_ip}:Host is down')
    except Exception as err_msg:
        print(f"ERROR:{err_msg}")




