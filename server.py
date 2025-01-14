from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Javobni qaytarish uchun status kodi va header'larni sozlash
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        # Javob mazmunini yozish
        self.wfile.write(b"ROUTE{Bu_Yo'l_Deganini_Aytyapti}")

# Serverni ishga tushirish
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=80):
    server_address = ('', port)  # Barcha interfeyslarda eshitish
    httpd = server_class(server_address, handler_class)
    print(f"Server ishlamoqda")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

