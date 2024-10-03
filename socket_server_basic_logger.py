import socket
import contextlib
from typing import cast #this is only for mypy type checking

class LogSocket:
    def __init__(self, socket: socket.socket):
        self._socket = socket
    
    def send(self, data):
        print(f"Sending: {data.decode('utf-8')}")
        return self._socket.send(data)
    
    def recv(self, bufsize):
        data = self._socket.recv(bufsize)
        print(f"Receiving: {data.decode('utf-8')}")
        return data

def dice_response(client_socket: socket.socket):
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Received request: {request}")
    # Respond with some dice roll simulation
    client_socket.send("Roll result: 4, 2, 6".encode('utf-8'))

def main_2() -> None:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 2401))
    server.listen(1)
    with contextlib.closing(server):
        while True:
            client, addr = server.accept()
            logging_socket = cast(socket.socket, LogSocket(client))  # Decorate the client socket
            dice_response(logging_socket)  # Use decorated socket in the same way
            client.close()

if __name__ == "__main__":
    main_2()
