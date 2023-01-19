# coding=utf-8
"""
    based on ICMP
"""

# add to the root path
import sys
import os
sys.path.append(os.path.dirname(__file__))                  # ..\HPScan\src\host_scan
sys.path.append(f"{os.path.dirname(__file__)}\\..\\")       # ..\HPScan\src
sys.path.append(f"{os.path.dirname(__file__)}\\..\\..\\")   # ..\HPScan

# module
import time
from HPScan.setting import *
from scapy.layers.inet import Ether,ICMP,IP
from scapy.layers.l2 import srp1


def icmp_scan(dst_ip, proxy_ip, proxy_port):
    """ICMP SCAN"""
    try:
        pkt = Ether() / IP(src=proxy_ip, dst=dst_ip) / ICMP(type=8) / b'hello?'  
        req = srp1(pkt, timeout=2, verbose=False)
        time.sleep(0.05)
        if req:
            ICMP_HOST_UP.append(dst_ip)
        else:
            pass
    except Exception as err_msg:
        print(f"error:{err_msg}")
        sys.exit(-1)