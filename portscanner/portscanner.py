import socket
from IPy import IP

ipaddress = input("[+] Enter Target To Scan: ")
port = 80

try:
    sock = socket.socket()
    sock.connect((ipaddress, port))
    print("[+] Port is Open...")
except:
    print("[-] Port is closed..")