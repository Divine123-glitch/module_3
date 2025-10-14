from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data=[
    {
        "name": "John Doe",
        "track": "Ai Engineering",
    }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=201                  ):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

        
    def do_POST(self):
        content_size = int(self.headers.get('Content-Length', 0))
        parsed_data = self.rfile.read(content_size)
        post_data = json.loads(parsed_data)
        data.append(post_data) # saving to a database
        self.send_data([
            {"message": "Data received successfully"},
            {"received_data": post_data}
        ], status=201)

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, BasicAPI)
    print('Starting server on port 8000...')
    httpd.serve_forever()
    
print("Running server...")
run()   