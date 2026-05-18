from http.server import HTTPServer, SimpleHTTPRequestHandler

from network.server.health.health_check import health_check, health_database_check


class ServerHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        routes = {
            '/health': self.handle_health,
            '/health_db': self.handle_health,
        }
        handler = routes.get(self.path, None)
        if handler:
            handler()
        else:
            super().do_GET()

    def handle_health(self):
        if health_check:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_error(503, 'Service Unavailable')

    def handle_health(self):
        if health_database_check:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_error(503, 'Database Unavailable')
            
    def send_error(self, code, message=None):
        self.send_response(code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message)

def start_http_server():
    port = 8383
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, ServerHandler)
    print(f"HTTP server running on port {port}...")
    httpd.serve_forever()