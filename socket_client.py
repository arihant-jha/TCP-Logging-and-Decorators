import socket

def request_data():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))  # Connect to server
    
    client_socket.send('roll_dice'.encode())  # Send request
    response = client_socket.recv(1024).decode()  # Receive response
    print(f"Server response: {response}")
    
    client_socket.close()

request_data()
