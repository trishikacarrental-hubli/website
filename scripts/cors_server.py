import http.server, functools, os
ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'site-optimized')
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
http.server.HTTPServer(('127.0.0.1', 8788), functools.partial(H, directory=ROOT)).serve_forever()
