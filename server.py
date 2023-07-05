import socket
import select

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Define the server address and port
server_address = ('localhost', 5555)

# Bind the server socket to the specified address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(2)  # Allow up to two players

# Maintain a list of connected clients and their respective teams
clients = []
teams = ["white", "black"]
team_index = 0

print("Server started. Waiting for connections...")

def broadcast(message, sender_socket):
    """Send a message to all connected clients except the sender."""
    for client in clients:
        if client != sender_socket:
            client.send(message)

while True:
    # Wait for activity on the server socket and connected client sockets
    sockets_list = [server_socket] + clients
    read_sockets, _, _ = select.select(sockets_list, [], [])

    for sock in read_sockets:
        # New connection request received
        if sock == server_socket:
            client_socket, client_address = server_socket.accept()
            clients.append(client_socket)
            print(f"New connection from {client_address}")

            # Assign team to the client
            if team_index < len(teams):
                team = teams[team_index]
                team_index += 1
                client_socket.send(team.encode())
            else:
                client_socket.send("The game is already full. Try again later.".encode())
                clients.remove(client_socket)
                client_socket.close()
                continue

            # Send a notification to all clients about the new team assignment
            broadcast(f"{team.capitalize()} team joined the game.", client_socket)

            # TODO: Handle game initialization

        # Incoming data from a client
        else:
            try:
                data = sock.recv(4096)
                if data:
                    # TODO: Process the received data (e.g., chess moves)
                    broadcast(data, sock)  # Send the move to all other clients
            except:
                print(f"Client {sock.getpeername()} disconnected")
                sock.close()
                clients.remove(sock)
                continue

server_socket.close()
