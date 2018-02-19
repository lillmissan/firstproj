import socket
import time

serversocket = socket.socket(socket.AF_INET)

serversocket.bind((socket.gethostname(), 6565))
serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()

    print("Connection established.")
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
