# coding:utf-8

import sys, os

sys.path.append(os.path.dirname(__file__))                  # ..\HPScan\src\port_scan
sys.path.append(f"{os.path.dirname(__file__)}\\..\\")       # ..\HPScan\src
sys.path.append(f"{os.path.dirname(__file__)}\\..\\..\\")   # ..\HPScan

import setting

from scapy.layers.inet import IP, TCP, Ether, ICMP
from scapy.all import *



def tcp_scan(dst_ip, dst_port, proxy_ip, proxy_port):
    """
    TCP SCAN: SYN scan
    """
    try:
        # 组装packet
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src=proxy_ip, dst=dst_ip)/TCP(sport=proxy_port, dport=dst_port, flags="S")
        response = srp1(pkt, timeout=2, verbose=False)
        time.sleep(0.01)
        # 响应为空
        if 'None' in str(type(response)):
            setting.CLOSED_PORTS.append(dst_port)
        elif response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12:
                # 0x12 => SYN+ACK
                setting.OPEN_PORTS.append(dst_port)
            elif response.getlayer(TCP).flags == 0x14:
                setting.CLOSED_PORTS.append(dst_port)
            else:
                # 其他情况下令当别论?
                pass
        elif response.haslayer(ICMP):
            # 差错检测报文 type3
            # 根据ICMP错误信息类型来判断端口状态
            if int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                setting.FILTERED_PORTS.append(dst_port)
        print(response)
    except Exception as err_msg:
        print(err_msg)
        sys.exit(-1)

tcp_scan(dst_ip='192.168.208.135', dst_port=80, proxy_ip='192.168.208.134', proxy_port=80)