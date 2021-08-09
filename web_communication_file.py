from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('hello Bar !', encode())


def main():
    PORT = 8090
    server = HTTPServer(('109.186.21.2', PORT), HelloHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
