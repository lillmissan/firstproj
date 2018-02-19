import socket
import sys

adress = ("192.168.197.104", 6565)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(adress)

while True:
    msg = raw_input("Message to server: ")
    s.sendto(msg)
    s.close()
