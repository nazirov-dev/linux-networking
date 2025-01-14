import socket


def start_server():
    host = "0.0.0.0"  # Mahalliy IP manzil
    port = 555  # Port raqami

    # Socketni yaratish
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        # IP va portni ulash
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server {host}:{port} da ishlayapti...")

        while True:
            # Ulanishni qabul qilish
            client_socket, client_address = server_socket.accept()
            print(f"Yangi ulanish: {client_address}")

            # Mijozdan ma'lumot kutish
            client_socket.recv(1024)  # Mijozdan xabar kutish
            message = "NC{Bunday_Ulanishlar!}\n"
            client_socket.sendall(message.encode('utf-8'))
            client_socket.close()
    except Exception as e:
        print(f"Xato yuz berdi: {e}")
    finally:
        # Server socketni yopish
        server_socket.close()


if __name__ == "__main__":
    start_server()
