# coding=utf-8
"""
    based on UDP
"""

# add to the root path
import sys
import os
sys.path.append(os.path.dirname(__file__))                  # ..\HPScan\src\host_scan
sys.path.append(f"{os.path.dirname(__file__)}\\..\\")       # ..\HPScan\src
sys.path.append(f"{os.path.dirname(__file__)}\\..\\..\\")   # ..\HPScan

# module 
import time
from setting import *
from scapy.layers.inet import Ether,IP,UDP
from scapy.all import srp1


def udp_scan(dst_ip, proxy_ip, proxy_port):
    """
    UDP SCAN: 
    """
    try:
        udp_msg = Ether()/IP(src=proxy_ip, dst=dst_ip)/UDP(sport=proxy_port, dport=DPORT)
        rece_msg = srp1(udp_msg, timeout=2, verbose=False)
        time.sleep(0.05)
        if rece_msg:
            UDP_HOST_UP.append(dst_ip)
    except Exception as err_msg:
        print(f"error:{err_msg}")
        sys.exit(-1)