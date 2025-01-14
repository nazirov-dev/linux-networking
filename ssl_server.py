import http.server
import socketserver

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # So'rovni ishlov berish
        message = "CURL{SSL_Sertifikatlar?_Bunga_Hech_Kimning_Vaqti_Yo‘q!}"
        
        # Javobni yuborish
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

# Serverni ishga tushurish
def run(server_class=http.server.HTTPServer, handler_class=MyHandler):
    port = 443
    server_address = ('0.0.0.0', port)  # Barcha interfeyslarda ishlash
    httpd = server_class(server_address, handler_class)
    print(f'Starting HTTP server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

