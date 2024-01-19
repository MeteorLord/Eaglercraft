import http.server
import socketserver
import os

# Set the directory where your HTML files are located
html_directory = "."

# Define the common port for all versions
port = 9000

# Change to the HTML directory
os.chdir(html_directory)

# Define a custom handler to serve files based on paths
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Map paths to corresponding HTML files
        if path == '/1.8':
            return os.path.join(html_directory, 'Eaglercraft-1.8.html')
        elif path == '/1.5':
            return os.path.join(html_directory, 'Eaglercraft-1.5.html')
        elif path == '/1.3':
            return os.path.join(html_directory, 'Eaglercraft-1.3.html')
        else:
            return super().translate_path(path)

    def end_headers(self):
        self.send_header('Content-Type', 'text/html')
        super().end_headers()

# Create a socket server for the specified port
with socketserver.TCPServer(("", port), CustomHandler) as httpd:
    print(f"Serving on port {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"Stopping server on port {port}")
