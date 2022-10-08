import socket
from _thread import *
import pickle

host = "127.0.0.1"
port = 55555
FORMAT = 'ascii'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(2)
YOUR_TURN = "YOUR_TURN"
turns = 0
clients,names = [],[]

def send_board(msg):
    for client in clients:
        client.send(msg)

def handle(client):
    turns = 0
    while True:
        try:
            if turns%2==0:
                clients[0].send("__WHITE MOVE__".encode(FORMAT))
                msg = clients[0].recv(1024)
                send_board(msg)
            else:
                clients[1].send("__BLACK MOVE__".encode(FORMAT))
                msg = clients[1].recv(1024)
                send_board(msg)

            turns+=1
        
        except:
            index = clients.index(client)
            name = names[index]
            names.remove(nickname)
            clients.remove(index)
            client.close()
            send_board(f"{name} has left the chat".encode(FORMAT))
            break