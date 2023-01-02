# coding:utf-8
"""
    Port_Scan
"""

# module use

from time import ctime
from scapy.layers.inet import IP, TCP, UDP
from scapy.all import *

from my_demo.module.helper import helper


# 扫某台主机的端口   支持b段和c段输入扫描
# ====>扫描的主机数大于1
# 对于每个主机均采用相同端口情况的扫描

class PortScan(helper):
    def __init__(self, alive_hosts, port='80', thread=10):
        super().__init__()
        self.hosts = alive_hosts  # 输入存活主机列表
        self.ports = helper.port_input(self, port)  # 输入扫描端口
        self.thread = thread

    def whole_scan(self):
        """TCP全开扫描"""
        for h in self.hosts:
            print(f"{ctime()}:scan {h}")
            for p in self.ports:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((h, p))
                    print(f'[+]{h}{p}/TCP open')
                    sock.close()
                except socket.error as err_msg:
                    text = sr1(IP(dst=h) / UDP(dport=p), timeout=5, verbose=0)
                    time.sleep(1)  # 防止太快而误判
                    if not text:
                        print(f'[+]{h}{p}/UDP open')
                    else:
                        print(f'[-]{h}{p}/TCP and UDP closed')

    # TCP半开的端口扫描技术
    # 应对目标主机的安全机制  防火墙设备  路由器规则 有可能会直接阻塞掉TCP的第一次连接请求
    # 但也有可能发送一个ICMP请求响应  可以根据ICMP请求响应的type和code字段进行判断
    def half_scan(self, dst_ip):
        """基于TCP半开的端口扫描"""
        src_port = RandShort()  # 源主机随机选取发送端口
        print(f"{ctime()}:scan {dst_ip}")
        for dst_port in self.ports:
            packet = IP(dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags="S")
            response = sr1(packet, timeout=1)
            print("half_scan")
            print(str(type(response)))

    def run(self):  # 多线程运行
        threads = []
        # 以主机为单位,为每台主机提供一个线程
        for h in self.hosts:
            t = threading.Thread(target=self.half_scan, args=(h,))
            threads.append(t)
        for i in range(0, len(threads)):
            threads[i].start()
        for i in range(0, len(threads)):
            threads[i].join()
