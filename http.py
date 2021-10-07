from http.server import BaseHTTPRequestHandler, HTTPServer
import time

host = "localhost"
port = 8080

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        html = f"<html><head></head><body><h1>Python HTTP</h1></body></html>"
        self.wfile.write(bytes(html, "utf8"))

if __name__ == "__main__":
    webServer = HTTPServer((host, port), Server)
    print("[HTTP Activated] http://%s:%s" % (host, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()