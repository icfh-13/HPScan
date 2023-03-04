
# coding:utf-8

import sys, os

sys.path.append(os.path.dirname(__file__))                  # ..\HPScan\src\port_scan
sys.path.append(f"{os.path.dirname(__file__)}\\..\\")       # ..\HPScan\src
sys.path.append(f"{os.path.dirname(__file__)}\\..\\..\\")   # ..\HPScan

import setting

from scapy.layers.inet import Ether, IP, UDP
from scapy.all import *

dst_ip = '192.168.208.135'
dst_port = 80
proxy_ip = '192.168.208.134'
proxy_port = 50050

def udp_scan(dst_ip, dst_port, proxy_ip, proxy_port):
    """
    UDP SCAN
    """
    try:
        pkt = Ether()/IP(src=proxy_ip, dst=dst_ip)/UDP(sport=proxy_port, dport=dst_port)
        response = srp1(pkt, timeout=2, verbose=False)
        time.sleep(0.05)
        print(response)
    except Exception as err_msg:
        print(err_msg)

udp_scan(dst_ip, dst_port, proxy_ip, proxy_port)