import socket
from IPy import IP

ipaddress = input('[+] Enter IP adress to scan: ')
port = 80

sock = socket.socket()
sock.connect(ipaddress, port)