import socket
import threading
import random

def handle_client(client_socket):
    # Receive the client's request
    request = client_socket.recv(1024).decode()
    
    # If request is 'roll_dice', generate dice rolls and send them back
    if request == 'roll_dice':
        dice_rolls = ', '.join([str(random.randint(1, 6)) for _ in range(5)])
        client_socket.send(dice_rolls.encode())  # Send the dice rolls
    
    # Close the client socket connection
    client_socket.close()
    # Thread will terminate automatically after this function completes

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(5)  # Allows 5 clients in the backlog queue
    print("Server listening on port 9999...")
    
    while True:
        # Accept new client connection
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        
        # Start a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()  # Thread starts, and the function `handle_client` runs

# Start the server
start_server()
