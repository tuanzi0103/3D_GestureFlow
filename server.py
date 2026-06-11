#!/usr/bin/env python3
"""
Local server for 云熠·星河
Run: python3 server.py
Then open: http://localhost:8080
"""
import http.server
import json
import os
import urllib.parse
from pathlib import Path

PORT = 8080
ROOT = Path(__file__).parent

ALLOWED_DIRS = {'photos', 'music', 'backgraph'}

IMAGE_EXT  = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.avif'}
AUDIO_EXT  = {'.mp3', '.mp4', '.m4a', '.mov', '.ogg', '.wav', '.flac', '.aac'}
BACK_EXT   = IMAGE_EXT


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        # Disable all caching so edits to index.html are always visible immediately
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/api/list':
            self._handle_list(parsed.query)
        else:
            super().do_GET()

    def _handle_list(self, query):
        params = urllib.parse.parse_qs(query)
        dir_name = params.get('dir', [''])[0]

        if dir_name not in ALLOWED_DIRS:
            self._json(400, {'error': 'invalid dir'})
            return

        target = ROOT / dir_name
        if not target.is_dir():
            self._json(200, [])   # folder doesn't exist yet → empty list
            return

        if dir_name == 'music':
            allowed_ext = AUDIO_EXT
        else:
            allowed_ext = IMAGE_EXT

        files = sorted(
            f.name for f in target.iterdir()
            if f.is_file() and f.suffix.lower() in allowed_ext
        )
        self._json(200, files)

    def _json(self, code, data):
        body = json.dumps(data).encode()
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(body))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        # suppress per-request logs, only show startup
        pass


if __name__ == '__main__':
    # Create the three folders if they don't exist
    for d in ALLOWED_DIRS:
        (ROOT / d).mkdir(exist_ok=True)

    print(f'云熠·星河 local server')
    print(f'  http://localhost:{PORT}')
    print(f'  Put files in:')
    print(f'    photos/    → photo cards')
    print(f'    music/     → background music')
    print(f'    backgraph/ → card back images')
    print(f'Press Ctrl+C to stop.\n')

    with http.server.ThreadingHTTPServer(('', PORT), Handler) as httpd:
        httpd.serve_forever()
