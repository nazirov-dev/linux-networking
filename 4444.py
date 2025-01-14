import socket
import time

def connect_to_server():
    host = "0.0.0.0"  # Server IP manzili
    port = 4444          # Server port raqami

    while True:
        try:
            # Mijoz socketini yaratish
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f"{host}:{port} ga ulanmoqchi...")

            # Serverga ulanish
            client_socket.connect((host, port))
            print("Serverga muvaffaqiyatli ulandi!")

            # 30 soniya kutish
            time.sleep(30)

            # Xabarni yuborish
            message = "NC{Endi_Men_Sizga_Ulanaman}\n"
            client_socket.sendall(message.encode('utf-8'))
            print(f"Xabar yuborildi: {message.strip()}")

            # Ulanishni yopish
            client_socket.close()
            print("Ulanish yopildi.")
        except Exception as e:
            print(f"Xato yuz berdi: {e}")
            time.sleep(10)

if __name__ == "__main__":
    connect_to_server()

