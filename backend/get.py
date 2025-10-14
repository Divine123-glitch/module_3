from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data=[
    {
        "name": "John Doe",
        "track": "Ai Engineering",
    }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
        
        
    def do_GET(self):
        self.send_data(data)
        
        

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, BasicAPI)
    print('Starting server on port 8000...')
    httpd.serve_forever()
    
print("Running server...")
run()   