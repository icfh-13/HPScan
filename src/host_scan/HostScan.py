# coding=utf-8
"""
    Host_Scan
"""

# add to the root path
import sys
import os
sys.path.append(os.path.dirname(__file__))                  # ..\HPScan\src\host_scan
sys.path.append(f"{os.path.dirname(__file__)}\\..\\")       # ..\HPScan\src
sys.path.append(f"{os.path.dirname(__file__)}\\..\\..\\")   # ..\HPScan

# module
from scapy.all import *
from src.helper.input import input
from src.helper.file_handler import get_proxy_ip, get_proxy_port

from src.host_scan.icmp_scan import icmp_scan
from src.host_scan.arp_scan import arp_scan
from src.host_scan.tcp_scan import tcp_scan
from src.host_scan.udp_scan import udp_scan


IP_LOG_PATH_FOR_HOSTSCAN = f"{os.path.dirname(__file__)}\..\..\log\ip_log"

class HostScan(input):
    def __init__(self, hosts, ports='80', mode='-icmp'):
        super().__init__()
        self.hosts = input.ip_input(self, hosts)        # 探测主机
        self.ports = ports                              # 端口
        self.mode = mode                                # 模式
        self.func = None                                # 模式下对应的函数调用

    def mode2func(self):
        if self.mode == '-icmp':
            self.func = icmp_scan
        elif self.mode == '-arp':
            self.func = arp_scan
        elif self.mode == '-tcp':
            self.func = tcp_scan
        elif self.mode == '-udp':
            self.func = udp_scan
        else:
            print("HOST SCAN MODE IS NOT MATCHED!")
            sys.exit(-1)

    def scan_threading(self):
        threads = []
        length = len(self.hosts)
        for ip in self.hosts:
            proxy_ip = get_proxy_ip(IP_LOG_PATH_FOR_HOSTSCAN)
            proxy_port = get_proxy_port(IP_LOG_PATH_FOR_HOSTSCAN)
            t = threading.Thread(target=self.func, args=(str(ip),str(proxy_ip),int(proxy_port)))
            threads.append(t)
        for i in range(length):
            threads[i].start()
        for i in range(length):
            threads[i].join()
    
def HOST_SCAN_RUN():
    



