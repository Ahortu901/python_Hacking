import socket
from IPy import IP


def scan_port(ipaddress, port):
    try:
        sock.settimeout(0.5)
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port " + str(port)  + " is Open...")
    except:
        print("[-] Port " + str(port) + " is closed..")

ipaddress = input("[+] Enter Target To Scan: ")
for port in range (70,85):
    scan_port(ipaddress, port)