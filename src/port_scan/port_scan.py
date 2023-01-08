# coding:utf-8
"""
    Port_Scan
    支持b段和c段扫描
"""

import sys, os

sys.path.append(os.getcwd())

# src use

from time import ctime
from scapy.layers.inet import IP, TCP, UDP
from scapy.all import *

from my_demo.src.helper.helper import input

# GLOBAL VAR

OPEN_PORT = []


class PortScan(input):
    def __init__(self, alive_hosts, port='80', thread=10):
        super().__init__()
        self.hosts = alive_hosts  # 输入存活主机列表
        self.ports = input.port_input(self, port)  # 输入扫描端口
        self.host_port_open = []
        self.host_port_close = []
        self.thread = thread

    def whole_scan(self, dst_ip):
        """TCP全开扫描"""
        print(f"{ctime()}:scan {dst_ip}")
        for dst_port in self.ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((dst_ip, dst_port))
                self.host_port_open.append(dst_ip + dst_port)
                sock.close()
            except socket.error as err_msg:
                text = sr1(IP(dst=dst_ip) / UDP(dport=dst_port), timeout=5, verbose=0)
                time.sleep(1)  # 防止太快而误判
                if not text:
                    self.host_port_open.append(dst_ip + ":" + dst_port)
                else:
                    self.host_port_close.append(dst_ip + ":" + dst_port)

    def half_scan(self, dst_ip):
        """基于TCP半开的端口扫描"""
        src_port = RandShort()  # 源主机随机选取发送端口
        print(f"{ctime()}:scan {dst_ip}")
        for dst_port in self.ports:
            try:
                pkt = IP(dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags="S")
                response = sr1(pkt, timeout=1)
                if response:
                    self.host_port_open.append(dst_ip + ":" + dst_port)
            except Exception as err_msg:
                continue

    def scan_threading(self):
        threads = []
        # 以主机为单位,为每台主机提供一个线程
        for h in self.hosts:
            t = threading.Thread(target=self.half_scan, args=(h,))
            threads.append(t)
        for i in range(0, len(threads)):
            threads[i].start()
        for i in range(0, len(threads)):
            threads[i].join()

    def run(self):
        print("-------Port_Scan Begin------")
        self.scan_threading()
        print("the open ports are as followed:")
        for open_port in self.host_port_open:
            print(open_port)
        print("the closed ports are as followed:")
        for closed_port in self.host_port_close:
            print(closed_port)
        print("-------Port_Scan End--------")
