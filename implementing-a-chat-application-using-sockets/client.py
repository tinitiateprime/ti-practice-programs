"""
This module implements a client for a chat application using sockets.

The client creates a socket object and connects to a server running on
localhost at port 5555. It then starts a separate thread to receive messages
from the server. The main thread waits for user input and sends it to the
server. The chat application is terminated when the user enters an empty line.
"""

import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    """
    Function to receive messages from the server.

    Args:
        client_socket (socket.socket): The socket object used for communication.

    Returns:
        None
    """
    while True:
        try:
            # Receive a message from the server and decode it
            message = client_socket.recv(1024).decode('utf-8')
            if message:  # If a message is received
                print(message)  # Print the received message
            else:
                break  # If no message is received, exit the loop
        except:
            continue  # If an exception occurs, continue to the next iteration

# Main function to start the client
def main():
    """
    Main function to start the client.

    Returns:
        None
    """
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client.connect(('127.0.0.1', 5555))

    # Start a thread to receive messages from the server
    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        # Read input from the user
        message = input()
        # Send the message to the server
        client.send(message.encode('utf-8'))

# Start the client
if __name__ == "__main__":
    main()