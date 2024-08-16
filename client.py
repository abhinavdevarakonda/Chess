#import game
import socket
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5555)

client_socket.connect(server_address)

while True:
    received_data = client_socket.recv(4096).decode()
    message = json.loads(received_data)

    if 'message' in message:
        print(message['message'])

        if message['message'] == 'Your turn':
            # TODO: Implement logic to get the player's move
            # my_move = game.board
            my_move = ['message']
            serialized_move = json.dumps(my_move)

            # send to server
            client_socket.send(serialized_move.encode())

    # TODO: Implement logic to update and display the game state 

client_socket.close()
