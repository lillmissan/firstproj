import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 6565))
tm = s.recv(1024)

s.close()

print("Time from machine: %s" % tm.decode('ascii'))
