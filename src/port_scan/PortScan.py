 # coding:utf-8
"""
    Port_Scan
"""

# add to the root path
import sys
import os
sys.path.append(os.path.dirname(__file__))                  # ..\HPScan\src\port_scan
sys.path.append(f"{os.path.dirname(__file__)}\\..\\")       # ..\HPScan\src
sys.path.append(f"{os.path.dirname(__file__)}\\..\\..\\")   # ..\HPScan

# module
from time import ctime
from scapy.layers.inet import IP, TCP, UDP
from scapy.all import *

import setting
from src.helper.input import input
from src.helper.file_handler import get_proxy_ip, get_proxy_port
from src.port_scan.tcp_scan import tcp_scan
from src.port_scan.udp_scan import udp_scan

IP_LOG_PATH_FOR_HOSTSCAN = f"{os.path.dirname(__file__)}\..\..\log\ip_log"

class PortScan(input):
    def __init__(self, mode = '-tcp', port='80', threads=10):
        super().__init__()
        self.hosts = setting.HOST_UP                # 输入存活主机列表
        self.ports = input.port_input(self, port)   # 输入扫描端口
        self.thread = threads
        self.mode = mode
        self.func = None

    def mode2func(self):
        if self.mode == '-tcp':
            self.func = tcp_scan
        elif self.mode == '-udp':
            self.func = udp_scan
        else:
            print("PORT SCAN MODE IS NOT MATCHED!")
            sys.exit(-1)

    def scan_threading(self):
        threads = []
        # 利用生成器不断返回代理ip和port
        ip_func = get_proxy_ip(IP_LOG_PATH_FOR_HOSTSCAN)
        port_func = get_proxy_port(IP_LOG_PATH_FOR_HOSTSCAN)
        # 以主机为单位,为每台主机提供一个线程
        for h in self.hosts:
            proxy_ip = next(ip_func)
            proxy_port = next(port_func)
            t = threading.Thread(target=self.half_scan, args=(h,))
            threads.append(t)
        for i in range(0, len(threads)):
            threads[i].start()
        for i in range(0, len(threads)):
            threads[i].join()


# def PORT_SCAN_RUN(PORT_SCAN):
#     PORT_SCAN.scan_threading()