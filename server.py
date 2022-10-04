import socket
from _thread import *
import pickle

host = "127.0.0.1"
port = 55555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(2)
YOUR_TURN = "YOUR_TURN"
turns = 0
clients,names = [],[]

def send_board(msg):
    for client in clients:
        client.send(msg)


