import socket
import select
import json

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 5555)

server_socket.bind(server_address)

server_socket.listen(2)  # max 2 players

clients = []
active_player = None

print("server started. waiting for players...")
main_board = []

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message)

while True:
    sockets_list = [server_socket] + clients
    read_sockets, _, _ = select.select(sockets_list, [], [])

    for sock in read_sockets:
        if sock == server_socket:
            client_socket, client_address = server_socket.accept()
            clients.append(client_socket)
            print(f"{client_address} connected.")

            welcome_message = {"message": "welcome!"}
            client_socket.send(json.dumps(welcome_message).encode())

            if not active_player:
                # first player to connect starts first (white)
                active_player = client_socket
                active_player.send(json.dumps({"message": "Your turn"}).encode())
            else:
                # tell the other player it's not their turn
                client_socket.send(json.dumps({"message": "Waiting for opponent's move"}).encode())

        else:
            try:
                data = sock.recv(4096).decode()
                if data:
                    received_list = json.loads(data)
                    main_board.append(received_list)
                    print(main_board)

                    # TODO: Process the received list object
                    # Example: Update the game state based on the received move

                    broadcast(json.dumps(received_list).encode(), sock)

                    if sock == active_player:
                        # change turn 
                        active_player = next((client for client in clients if client != active_player), None)
                        if active_player:
                            active_player.send(json.dumps({"message": "Your turn"}).encode())
            except:
                print(f"Client {sock.getpeername()} disconnected")
                sock.close()
                clients.remove(sock)
                if sock == active_player:
                    active_player = None
                continue

# Close the server socket
server_socket.close()
