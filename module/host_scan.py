# coding=utf-8
"""
    Host_Scan
"""

# module use
from my_demo.module.helper import helper
from scapy.layers.inet import *
from scapy.layers.l2 import *
from scapy.all import *


class HostScan(helper):
    def __init__(self, hosts, ports='80'):
        super().__init__()
        self.count = 0
        self.hosts = helper.ip_input(self, hosts)
        self.ports = ports
        self.alive_hosts = []

    # 是单纯的去扫描  还是已经拿到内网的一台主机 然后去扫描？
    def arp_req(self, ip):
        pass

    def icmp_req(self, ip):  # 使用icmp数据包来进行内网主机存活探测
        """using icmp to scan the alive host"""
        try:
            # 以太层/目标地址/ICMP报文类型为请求报文/传输的字节码
            package = Ether() / IP(dst=ip) / ICMP(type=8) / b'how_are_you?'  # 构造数据包
            req = srp1(package, timeout=2, verbose=False)
            if req:
                print(f'[+]{ip}:Host is up')
                self.alive_hosts.append(ip)
                self.count += 1
            else:
                print(f'[-]{ip}:Host is down')
        except Exception as err_msg:
            print(f"ERROR:{err_msg}")

    # 多线程运行
    def hostscan_threading(self):
        threads = []
        length = len(self.hosts)
        for ip in self.hosts:
            t = threading.Thread(target=self.icmp_req, args=(str(ip),))
            threads.append(t)
        # 多线程
        for i in range(length):
            # print(f"{i}:")
            threads[i].start()
        # 阻塞
        for i in range(length):
            threads[i].join()

    def run(self):
        print("-------Host_Scan Begin------")
        self.hostscan_threading()
        print(f"result: {self.count} hosts are alive")
        for a_h in self.alive_hosts:
            print(a_h)
        print("-------Host_Scan End------")
