import http.server
import requests

class ProxyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Proxy received request: {self.path}")
        print(f"Headers: {self.headers}")

        try:
            # So'rovni mijoz serverga yuborish
            response = requests.get(self.path, headers={"X-Proxy": "Custom-Proxy"})

            # Mijoz server javobini qaytarish
            self.send_response(response.status_code)
            self.end_headers()
            self.wfile.write(response.content)
        except Exception as e:
            print(f"Error while forwarding request: {e}")
            self.send_response(500)
            self.end_headers()

if __name__ == "__main__":
    server_address = ('0.0.0.0', 3128)
    httpd = http.server.HTTPServer(server_address, ProxyHTTPRequestHandler)
    print(f"Proxy server running on {server_address[0]}:{server_address[1]}")
    httpd.serve_forever()

