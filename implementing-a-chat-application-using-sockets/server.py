"""
This module implements a server for a chat application using sockets.

The server listens for incoming connections on localhost at port 5555.
When a client connects, the server adds the client to a list of connected clients.
The server then starts a new thread to handle the client's messages.
The server continuously listens for incoming connections and handles client messages in separate threads.
"""

import socket
import threading

# List to store all connected clients
clients = []


def handle_client(client_socket):
    """
    Function to handle client connections.

    Args:
        client_socket (socket.socket): The socket object used for communication.

    Returns:
        None
    """
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                # Broadcast the message to all connected clients except the client who sent the message
                broadcast_message(message, client_socket)
            else:
                # Remove the client from the list of connected clients
                remove_client(client_socket)
                break
        except:
            continue


def broadcast_message(message, client_socket):
    """
    Function to broadcast the message to all connected clients except the client who sent the message.

    Args:
        message (str): The message to be broadcasted.
        client_socket (socket.socket): The socket object of the client who sent the message.

    Returns:
        None
    """
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                # Remove the client from the list of connected clients if the client is not able to receive the message
                remove_client(client)


def remove_client(client_socket):
    """
    Function to remove a client from the list of connected clients.

    Args:
        client_socket (socket.socket): The socket object of the client to be removed.

    Returns:
        None
    """
    if client_socket in clients:
        clients.remove(client_socket)


def main():
    """
    Main function to start the server.

    Returns:
        None
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    server.bind(('127.0.0.1', 5555))  # Bind the server to localhost and port 5555
    server.listen(5)  # Listen for incoming connections
    print('Server started, waiting for clients...')

    while True:
        client_socket, addr = server.accept()  # Accept a new client connection
        clients.append(client_socket)  # Add the client to the list of connected clients
        print(f'Client {addr} connected')
        threading.Thread(target=handle_client, args=(client_socket,)).start()  # Start a new thread for the client


# Start the server when the script is executed directly
if __name__ == "__main__":
    main()