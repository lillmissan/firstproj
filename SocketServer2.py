import socket
import sys
adress = ("192.168.197.104", 6565)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(adress)

while True:
    data, addr = s.recvfrom(2048)
    print data, addr
    s.close()
