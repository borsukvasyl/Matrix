from http.server import HTTPServer, CGIHTTPRequestHandler
from webbrowser import open
server_address = ("", 5000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
open('http://localhost:5000')
httpd.serve_forever()

