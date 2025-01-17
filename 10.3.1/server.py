import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Define the IP address and bridge name
        ip_to_check = "172.16.50.0"
        bridge_name = "br-5720f05dd68a"
        
        # Check if the IP is assigned to the bridge
        try:
            result = subprocess.run(
                ["ip", "addr", "show", bridge_name],
                capture_output=True,
                text=True,
                check=True
            )
            if ip_to_check in result.stdout:
                response_message = 'ROUTE{Bu_Yo\'l_Deganini_Aytyapti}'
            else:
                response_message = 'Vazifa bajarilmadi'
        except subprocess.CalledProcessError:
            response_message = 'Error checking IP address'

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response_message.encode())

if __name__ == '__main__':
    server_address = ('0.0.0.0', 80)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server on port 80...')
    httpd.serve_forever()