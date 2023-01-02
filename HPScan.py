# coding=utf-8

import sys, os
CUR_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.split(CUR_PATH)[0]
sys.path.append(ROOT_PATH)

# module
import argparse
from module.helper import helper
from module.host_scan import HostScan
from module.port_scan import PortScan
#from module.ip_proxy_pool import *

describe = '''
-------------------------
|    PHScan             |
|                       |
|    python 3.10        |
-------------------------
'''

# terminal input
# parser = argparse.ArgumentParser(description="HPScan")
# parser.add_argument('-host', dest='host', help="please input host", required=True)
# parser.add_argument('-port', dest='port', help="please input port", default=80)
# parser.add_argument('-mode', dest='mode', help="please input mode")
# args = parser.parse_args()
19
# run
if __name__ == '__main__':
    print(describe)
    temp_host = "192.168.208.129"
    temp_port = "0-100"
    # temp_host = input("Please input your host:")
    # temp_port = input("Please input your port:")
    # port_obj = PortScan(['192.168.208.128'], args.port)
    # temp_host = args.host
    # temp_port = args.port

    if temp_host:
        host_obj = HostScan(temp_host, temp_port)
        host_obj.run()
    if temp_port:
        port_obj = PortScan(host_obj.alive_hosts, temp_port)
        port_obj.run()
