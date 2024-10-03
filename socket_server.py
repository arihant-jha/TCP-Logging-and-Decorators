import socket
import random

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(1)
    print("Server listening on port 9999...")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        request = client_socket.recv(1024).decode()  # Receive client request
        
        if request == 'roll_dice':
            dice_rolls = ', '.join([str(random.randint(1, 6)) for _ in range(5)])
            client_socket.send(dice_rolls.encode())  # Send random dice rolls
        client_socket.close()

start_server()