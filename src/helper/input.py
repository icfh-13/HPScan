"""
    INPUT CLASS
"""

import sys


class input:
    """This is a class which was created to help input"""

    def __init__(self, scan_host="", scan_ports="80"):
        self.scan_host = self.ip_input(scan_host)
        self.scan_ports = self.port_input(scan_ports)

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
                if len(ip.split('.')) == 4:
                    '''ip C segment'''
                    iplist.append(ip_prefix.join(str(i)))
                elif len(ip.split('.')) == 3:
                    '''ip B segment'''
                    for j in range(1, 255):
                        iplist.append(ip_prefix + str(i) + "." + str(j))
                else:
                    sys.exit("ip-InputError")
        return iplist

    def port_input(self, port):
        portlist = []
        if ',' in str(port):
            '''for some specific ports'''
            portlist = [int(p) for p in port.split(',')]
        elif len(port.split('-')) == 1:
            '''for the port you want'''
            portlist.append(int(port))
        elif len(port.split('-')) == 2:
            '''for a range of ports'''
            p_start, p_end = int(port.split('-')[0]), int(port.split('-')[1])
            portlist = [int(p) for p in range(p_start, p_end + 1)]
        else:
            sys.exit("port-InputError")
        return portlist