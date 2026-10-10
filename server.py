"""Serve the browser app locally without requiring third-party packages."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser

HOST = "127.0.0.1"
PORT = 8000


def run_server() -> None:
    """Serve the project files on localhost and open the app in a browser."""
    project_dir = Path(__file__).resolve().parent
    handler = partial(SimpleHTTPRequestHandler, directory=str(project_dir))
    url = f"http://{HOST}:{PORT}"

    with ThreadingHTTPServer((HOST, PORT), handler) as server:
        print(f"Gen-Z Consultant is running at {url} (press Ctrl+C to stop)")
        webbrowser.open(url, new=2)

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping Gen-Z Consultant.")


if __name__ == "__main__":
    run_server()
