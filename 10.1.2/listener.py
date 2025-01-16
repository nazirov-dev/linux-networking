import socket
import threading

# List of ports to listen on
ports = [21, 22, 8888, 3138, 443, 1024, 2222, 80]

# Function to handle a single port
def start_server(port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", port))
        server_socket.listen(5)

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address} on port {port}")
            client_socket.sendall(b"Hello! You've connected to the server.\n")
            client_socket.close()
    except Exception as e:
        print(f"Error on port {port}: {e}")

# Start a thread for each port
threads = []
for port in ports:
    thread = threading.Thread(target=start_server, args=(port,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()