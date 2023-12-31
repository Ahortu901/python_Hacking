import socket
from IPy import IP

def scan(target, port_num):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning Target] ' + str(target))
    for port in range (1, int(port_num)):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+]Open port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+]Open port ' + str(port))
    except:
        pass

targets = input("[+] Enter Target/s To Scan(split multiple targets with ,): ")
port_num = input("[+] Enter the number of ports to scan: ")
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '), port_num)
else:
    scan(targets, port_num)
