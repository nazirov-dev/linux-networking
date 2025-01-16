import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 555))
s.listen(5)

while True:
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    conn.close()
