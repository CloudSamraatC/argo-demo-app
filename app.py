from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>GitOps App</title>
        </head>
        <body style="font-family: Arial; text-align:center; margin-top:50px;">
            <h1>🚀 Welcome to GitOps!</h1>
            <p>Application is running successfully.</p>
            <p>Triggered by GitHub, deployed automatically by ArgoCD.</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())
#
class MyServer:
    def __init__(self, host="0.0.0.0", port=8080):
        self.host = host
        self.port = port
        self.server = HTTPServer((host, port), MyHandler)

    def start(self):
        print(f"Server starting on http://{self.host}:{self.port}")
        self.server.serve_forever()

    def stop(self):
        self.server.shutdown()
        print("Server stopped")


if __name__ == "__main__":
    try:
        server = MyServer(port=8080)
        server.start()

    except KeyboardInterrupt:
        print("\nReceived Ctrl+C")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        try:
            server.stop()
        except:
            pass
