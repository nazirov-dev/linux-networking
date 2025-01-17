import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Define the flag to return if conditions are met
        response_message = b"\nROUTE{Bu_Yo'l_Deganini_Aytyapti}\n"
        # Send response
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(response_message)
        except BrokenPipeError:
            pass

def check_ip_assigned(ip_to_check, bridge_name):
    """
    Check if the given IP is assigned to the specified bridge interface.
    """
    try:
        result = subprocess.run(
            ["ip", "addr", "show", bridge_name],
            capture_output=True,
            text=True,
            check=True
        )
        return ip_to_check in result.stdout
    except subprocess.CalledProcessError:
        return False

def run_server(ip_address, port):
    """
    Run the HTTP server.
    """
    server_address = (ip_address, port)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

def main():
    # Define the bridge interface and target IP
    target_ip = "172.16.50.10"
    bridge_name = "br-5720f05dd68a"

    while True:
        if check_ip_assigned('172.16.50.0', bridge_name):
            try:
                run_server(target_ip, 80)
            except Exception as e:
                print(f"Server error: {e}")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()