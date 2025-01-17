import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # IP va bridge nomi
        ip_to_check = "172.16.50.0/24"
        bridge_name = "br-5720f05dd68a"
        
        # Javob xabari uchun o'zgaruvchi
        response_message = ""
        
        try:
            # `ip` komandasi orqali bridge ni tekshirish
            result = subprocess.run(
                ["ip", "route", "show", "dev", bridge_name],
                capture_output=True,
                text=True,
                check=True
            )
            # Agar kerakli IP natijada bo'lsa
            if ip_to_check in result.stdout:
                response_message = "\nROUTE{Bu_Yo'l_Deganini_Aytyapti}\n"
            else:
                response_message = "\nVazifa bajarilmadi: IP topilmadi.\n"
        except subprocess.CalledProcessError as e:
            response_message = f'Error: {e}'
        
        # HTTP responseni yuborish
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(response_message.encode())
        except BrokenPipeError:
            pass  # Ulanish to'satdan uzilib qolsa, e'tiborga olinmaydi

def run_server():
    server_address = ('172.16.50.10', 80)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Running server on port 80...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server to'xtatildi.")
    finally:
        httpd.server_close()

if __name__ == "__main__":
    run_server()
