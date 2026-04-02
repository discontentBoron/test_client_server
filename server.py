import socket
import threading

HOST = '0.0.0.0'
PORT = 5000

def handle_client(conn, address):
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"From {address}: {data}")
        response = input(' -> ')
        conn.send(response.encode())
    conn.close()
    print(f"Connection closed: {address}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(2)

print("Server listening...")

while True:
    conn, address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, address))
    thread.daemon = True
    thread.start()