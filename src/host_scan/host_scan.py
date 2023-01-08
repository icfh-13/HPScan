# coding=utf-8
"""
    Host_Scan
"""

import sys, os
sys.path.append(os.getcwd())

# src use
from HPScan.src.helper.input import input
from scapy.layers.inet import *
from scapy.layers.l2 import *
from scapy.all import *



class HostScan(input):
    def __init__(self, hosts, ports='80'):
        super().__init__()
        self.count = 0
        self.hosts = input.ip_input(self, hosts)
        self.ports = ports
        self.alive_hosts = []

    def arp_req(self, ip):
        pass

    def icmp_req(self, ip):
        """ICMP SCAN"""
        try:
            pkt = Ether() / IP(dst=ip) / ICMP(type=8) / b'hello?'  # 构造数据包
            req = srp1(pkt, timeout=2, verbose=False)
            if req:
                print(f'[+]{ip}:Host is up')
                self.alive_hosts.append(ip)
                self.count += 1
            else:
                print(f'[-]{ip}:Host is down')
        except Exception as err_msg:
            print(f"ERROR:{err_msg}")

    def scan_threading(self):
        threads = []
        length = len(self.hosts)
        for ip in self.hosts:
            t = threading.Thread(target=self.icmp_req, args=(str(ip),))
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


