# coding=utf-8
"""
    Host_Scan
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# src use
from HPScan.src.helper.input import input
from scapy.all import *
from icmp_scan import icmp_scan
from arp_scan import arp_scan

IP_LOG_PATH = f"{os.getcwd()}\..\..\log\ip_log"

class HostScan(input):
    def __init__(self, hosts, ports='80', mode='-icmp'):
        super().__init__()
        self.count = 0                                  # 存活主机数目
        self.hosts = input.ip_input(self, hosts)        # 探测主机
        self.ports = ports                              # 端口
        self.alive_hosts = []                           # 存活主机列表
        self.mode = mode                                # 模式
        self.func = None                                # 模式下对应的函数调用

    def mode2func(self):
        if self.mode == 'icmp':
            self.func = icmp_scan
        elif self.mode == 'arp':
            self.func = arp_scan


    def scan_threading(self):
        threads = []
        length = len(self.hosts)
        for ip in self.hosts:
            t = threading.Thread(target=self.func, args=(str(ip),))
            threads.append(t)
        for i in range(length):
            threads[i].start()
        for i in range(length):
            threads[i].join()

    def run(self):
        print("-------Host_Scan Begin------")
        self.scan_threading()
        print(f"result: {self.count} hosts are alive")
        print(f"alive hosts are as followed:")
        for host in self.alive_hosts:
            print(host)
        print("-------Host_Scan End------")


