from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

# Fayllar saqlangan asosiy papka
BASE_DIR = "/root/wget_server"  # Sizning test papkangiz yo'li

# Papka ichidagi fayllarni servis qilish uchun handler
class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Fayllarni asosiy katalog ichida qidirish
        root = os.path.abspath(BASE_DIR)
        return os.path.join(root, *path.split("/"))

# Serverni ishga tushirish
PORT = 80
Handler = CustomHTTPRequestHandler

with TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started at http://0.0.0.0:{PORT}")
    print(f"Serving files from: {os.path.abspath(BASE_DIR)}")
    httpd.serve_forever()

