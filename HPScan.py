# coding=utf-8


# module
import argparse
# from my_demo.module.helper import helper
from my_demo.module.host_scan import HostScan
from my_demo.module.port_scan import PortScan

describe = '''
-------------------------
|    PHScan             |
|                       |
|    python 3.10        |
-------------------------
'''

# terminal input
parser = argparse.ArgumentParser(description="HPScan")
parser.add_argument('-host', dest='host', help="please input host", required=True)
parser.add_argument('-port', dest='port', help="please input port", default=80)

args = parser.parse_args()

# run
if __name__ == '__main__':
    print(describe)
    temp_host = input("Please input your host:")
    temp_port = input("Please input your port:")
    host_obj = HostScan(temp_host, temp_port)
    host_obj.run()
    # port_obj = PortScan(['192.168.208.128'], args.port)
    port_obj = PortScan(host_obj.alive_hosts, temp_port)
    port_obj.run()
