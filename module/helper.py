# coding:utf-8
"""
    helper.py:
    1.helper_class with ip_input and port_input method
    2.file writer and reader function
"""

# module use
import sys


class helper:
    """This is a class which was created to help input"""

    def __init__(self, scan_host="", scan_ports="80"):
        self.scan_host = self.ip_input(scan_host)               # str->list
        self.scan_ports = self.port_input(scan_ports)           # str->list

    def ip_input(self, ip):
        """Determine whether it is an IP or an IP segment"""
        ip_flag = len(ip.split('-'))
        iplist = []
        if ip_flag == 1:
            iplist.append(ip)
            return iplist
        else:
            ip_prefix = ip.split('-')[0][:-len(ip.split('-')[0].split('.')[-1])]
            start = int(ip.split('-')[0].split('.')[-1])
            end = int(ip.split('-')[1])
            for i in range(start, end):
                if len(ip.split('.')) == 4:                         # 支持C段输入
                    iplist.append(ip_prefix.join(str(i)))
                elif len(ip.split('.')) == 3:                       # 支持B段输入
                    for j in range(1, 255):
                        iplist.append(ip_prefix + str(i) + "." + str(j))
                else:
                    sys.exit("ip-InputError")
        return iplist

    def port_input(self, port):
        """Supports scanning for specific ports and port ranges"""
        portlist = []
        if ',' in str(port):                                             # 特定的几个端口
            portlist = [int(p) for p in port.split(',')]
        elif len(port.split('-')) == 1:                             # 一个端口
            portlist.append(int(port))
        elif len(port.split('-')) == 2:                             # 端口范围
            p_start, p_end = int(port.split('-')[0]), int(port.split('-')[1])
            portlist = [int(p) for p in range(p_start, p_end + 1)]
        else:
            sys.exit("port-InputError")
        return portlist


def writer(filename, text, mode):
    try:
        if 'b' in mode:                                                     # 涉及二进制文件
            with open(file=filename, mode=mode) as f:
                f.write(text)
                f.write('\n')
        else:
            with open(file=filename, mode=mode, encoding='utf-8') as f:
                f.write(text)
                f.write('\n')
    except:
        print("file write error!")
        sys.exit(-1)


def reader(filename):
    with open(file=filename, mode='r') as f:
        text = f.read()
    return text
