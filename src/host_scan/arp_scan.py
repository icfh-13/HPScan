# coding=utf-8
"""
    based on ARP
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
from scapy.layers.inet import Ether
from scapy.layers.l2 import ARP,srp1
 
def arp_scan(dst_ip, proxy_ip, proxy_port):
    """
    ARP_SCAN
    """
    arp_msg = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, psrc=proxy_ip, pdst=dst_ip)
    try:
        rece_msg = srp1(arp_msg, timeout=2, verbose=0)[1]
        time.sleep(0.05)
        if rece_msg:
            ARP_HOST_UP.append(dst_ip)
    except Exception as err_msg:
        print(f"error:{err_msg}")
        sys.exit(-1)





