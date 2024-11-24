import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class FileUploadHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_PUT(self):
        # Extract the file name from the URL path
        filename = os.path.basename(self.path)
        
        # If no filename is found, reject the request
        if filename == "" or filename == "/":
            self.send_response(400, "Bad Request")
            self.end_headers()
            self.wfile.write(b"File name is missing in the request URL.")
            return

        # Set the target file path to the current working directory
        target_directory = os.getcwd()  # Use the current working directory
        path = os.path.join(target_directory, filename)

        # Ensure the directory exists, if not create it
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Read and write the file content
        length = int(self.headers['Content-Length'])
        with open(path, 'wb') as f:
            f.write(self.rfile.read(length))

        # Send response back to the client
        self.send_response(201, "Created")
        self.end_headers()
        self.wfile.write(f"File {filename} uploaded successfully.".encode())

def run(server_class=HTTPServer, handler_class=FileUploadHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on 0.0.0.0 port {port} (http://0.0.0.0:{port}/) ...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
