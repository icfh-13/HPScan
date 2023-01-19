# coding=utf-8
"""
    based on TCP 
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
from scapy.layers.inet import Ether,IP,TCP
from scapy.all import srp1



def tcp_scan(dst_ip, proxy_ip, proxy_port):
    """
    TCP SCAN: send packet with SYN to the host
    """
    try:
        tcp_msg = Ether()/IP(src=proxy_ip,dst=dst_ip)/TCP(sport=proxy_port, dport=DPORT)
        rece_msg = srp1(tcp_msg, timeout=2, verbose=False)
        time.sleep(0.05)
        if rece_msg:
            TCP_HOST_UP.append(dst_ip)
    except Exception as err_msg:
        print(f"error:{err_msg}")
        sys.exit(-1)