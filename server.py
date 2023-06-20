import socket
import os
from _thread import *

serverSocket = socket.socket()
host = "127.0.0.1"
port = 5555
threadCount = 0

#connecting host and port to server
try:
    serverSocket.bind((host,port))
except socket.error as e:
    print(str(e))

print(f"LISTENING ON {serverSocket}")
serverSocket.listen(5)

def multi_threaded_client(connection):
    connection.send(str.encode("server is working"))
    while True:
        data = connection.recv(2048)
        response = "server message: " + data.decode('utf-8')
        if not data:
            break

        connection.sendall(str.encode(response))
    connection.close()

while True:
    Client, addr = serverSocket.accept()
    print("CONNECTED TO: " + addr[0] + ":" + str(addr[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    threadCount += 1
    print("thread number: " + str(threadCount))

serverSocket.close()