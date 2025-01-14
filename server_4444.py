import socket

# Flag ma'lumotlari
flag_message = "SOCAT{TAG_Siz_Buysiz!}\n"

# Doimiy server
while True:
    try:
        # Soketni sozlash
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', 4444))  # 4444-portni tinglaymiz
        s.listen(5)
        print("Listening on port 4444...")

        # Ulanishni qabul qilish
        conn, addr = s.accept()
        print(f"Connection from {addr}")

        # Flag xabarini yuborish
        conn.sendall(flag_message.encode('utf-8'))

        # Ulanishni yopish
        conn.close()
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        try:
            s.close()
        except:
            pass
        print("Restarting server...")

