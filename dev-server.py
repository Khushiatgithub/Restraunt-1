import http.server
import socketserver
import os
import mimetypes

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        # Extract base path without query parameters or hash
        base = path.split('?')[0].split('#')[0]
        # Check if there is an '@' in the filename
        if '@' in base:
            filename = os.path.basename(base)
            name_part, sep, _ = filename.partition('@')
            # Use the part before '@' to guess the mime type
            guessed_type, _ = mimetypes.guess_type(name_part)
            if guessed_type:
                return guessed_type
        return super().guess_type(path)

    def do_GET(self):
        # Translate the URL path to a local file system path
        local_path = self.translate_path(self.path)
        
        # Clean path to check prefixes
        clean_path = self.path.split('?')[0].split('#')[0]
        
        # If the file does not exist locally and is an asset/upload, redirect to live site
        if not os.path.exists(local_path):
            is_wp_asset = clean_path.startswith(('/wp-content/', '/wp-includes/'))
            is_media = clean_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.pdf', '.mp4', '.woff', '.woff2', '.ttf', '.otf', '.ico'))
            
            if is_wp_asset or is_media:
                live_url = "https://tanatan.co" + self.path
                self.send_response(302)
                self.send_header('Location', live_url)
                self.end_headers()
                return
                
        super().do_GET()

PORT = 8080
Handler = CustomHandler

# Enable port reuse
socketserver.TCPServer.allow_reuse_address = True

print(f"Starting server on port {PORT}...")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving HTTP on port {PORT} (http://localhost:{PORT}/)...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
