# Implementing a Chat Application Using Sockets
* Develop a simple chat application using Python sockets. The application should allow multiple clients to connect to a server and send messages to each other.

# Chat Application
This project implements a simple chat application using sockets in Python. It consists of a server and a client module. The server handles multiple clients, allowing them to communicate with each other.

## Files

- `client.py`: Contains the code for the chat client.
- `server.py`: Contains the code for the chat server.

## client.py
### Description
This module implements a client for a chat application using sockets. The client connects to a server running on localhost at port 5555 and starts a separate thread to receive messages from the server. The main thread waits for user input and sends it to the server. The chat application terminates when the user enters an empty line.

### Functions
#### `receive_messages(client_socket)`
Receives messages from the server and prints them.

##### Arguments

- `client_socket` (socket.socket): The socket object used for communication.

##### Description

- Continuously receives messages from the server.
- Decodes and prints received messages.
- Exits the loop if no message is received.

#### `main()`
Starts the client.

##### Description

- Creates a socket object.
- Connects to the server.
- Starts a thread to receive messages from the server.
- Continuously reads input from the user and sends it to the server.

### Usage
```bash
python client.py

```
## server.py
### Description
This module implements a server for a chat application using sockets. The server listens for incoming connections on localhost at port 5555. When a client connects, the server adds the client to a list of connected clients and starts a new thread to handle the client's messages. The server continuously listens for incoming connections and handles client messages in separate threads.

### Functions
#### `handle_client(client_socket)`
Handles client connections.

##### Arguments

- `client_socket` (socket.socket): The socket object used for communication.

##### Description

- Continuously receives messages from the client.
- Broadcasts the received message to all connected clients except the client who sent the message.
- Removes the client from the list of connected clients if no message is received.

#### `broadcast_message(message, client_socket)`
Broadcasts the message to all connected clients except the client who sent the message.

##### Arguments

- `message` (str): The message to be broadcasted.
- `client_socket` (socket.socket): The socket object of the client who sent the message.

#### `remove_client(client_socket)`
Removes a client from the list of connected clients.

##### Arguments

- `client_socket` (socket.socket): The socket object of the client to be removed.

#### `main()`
Starts the server.

##### Description

- Creates a TCP socket.
- Binds the server to localhost and port 5555.
- Listens for incoming connections.
- Accepts new client connections and starts a new thread for each client.

### Usage
```bash
python server.py

```