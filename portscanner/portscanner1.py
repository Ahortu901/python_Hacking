import socket
from IPy import IP

ipaddress = input('[+] Enter IP adress to scan: ')
port = 80

try:
    sock = socket.socket()
    sock.connect(ipaddress, port)
    print('[+]Port is opened')
except:
    print('[-]Port is closed...')