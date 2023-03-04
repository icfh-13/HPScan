"""
CONFIG AND GLOBAL VAR
"""
from time import ctime


# IP PROXY POOL 
URLs = {
    '免费代理IP': 'http://ip.yqie.com/ipproxy.htm',  
    '66免费代理网': 'http://www.66ip.cn/',  
    '89免费代理': 'http://www.89ip.cn/',  
    '云代理': 'http://www.ip3366.net/',  
    '快代理': 'https://www.kuaidaili.com/free/'  
}
IP_COUNT = 1000                         # 爬取的IP数量设置
TEST_URL = "http://www.baidu.com"       # 测试网站
FILE_NAME = ctime()                     # ip日志生成文件名


# HOST SCAN：

DPORT = 80

CLOSED_HOST = []

OPEN_HOST = []

ICMP_OPEN_HOST = []   ## ICMP SCAN 

ARP_OPEN_HOST = []    ## ARP SCAN

TCP_OPEN_HOST = []    ## TCP SYN SCAN 

UDP_OPEN_HOST = []    ## UDP SCAN

# PORT SCAN:

# 若没有指定扫描端口，则启动默认端口
DEFALUT_PORTS = [21, 22, 23, 80, 443]      


"""
21/tcp FTP 文件传输协议

22/tcp SSH 安全登录、文件传送(SCP)和端口重定向

23/tcp Telnet 不安全的文本传送

25/tcp SMTP Simple Mail Transfer Protocol (E-mail)

69/udp TFTP Trivial File Transfer Protocol

79/tcp finger Finger

80/tcp HTTP 超文本传送协议 (WWW)

88/tcp Kerberos Authenticating agent

110/tcp POP3 Post Office Protocol (E-mail)

113/tcp ident old identification server system

119/tcp NNTP used for usenet newsgroups

220/tcp IMAP3

443/tcp HTTPS used for securely transferring web pages
"""


OPEN_PORTS = []

CLOSED_PORTS = []

FILTERED_PORTS = []

UNFILTERED_PORTS = []

OPEN_OR_FILTERED_PORTS = []

CLOSED_OR_FILTERED_PORTS = []

