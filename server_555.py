import socket
import os

# Flag ma'lumotlari
flag_content = "SOCAT{SOCAT_Bilan_Ulangan}"
flag_path = "/tmp/flag.txt"

# Doimiy server
while True:
    try:
        # Soketni sozlash
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', 555))  # 555-portni tinglaymiz
        s.listen(5)
        print("Listening on port 555...")

        # Ulanishni qabul qilish
        conn, addr = s.accept()
        print(f"Connection from {addr}")

        # Flag faylini yaratish
        if not os.path.exists(flag_path):
            with open(flag_path, "w") as f:
                f.write(flag_content)
            print(f"Flag file created at {flag_path}")

        # Ulanishni boshqarish
        conn.close()
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        try:
            s.close()
        except:
            pass
        print("Restarting server...")

