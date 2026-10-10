# Gen-Z Consultant

A lightweight, browser-based chat UI for a playful Gen-Z style consultant.
Replies are selected at random from a built-in list; this demo does not connect
to an AI model or send messages to an external service.

## Run the app

```bash
python genz_consultant.py
```

The launcher starts a local web server and opens the app in your default
browser. Keep the terminal open while using the app; press `Ctrl+C` there to
stop the server. If the browser does not open automatically, visit:

```text
http://127.0.0.1:8000
```

You can also run `python server.py` to start the server directly.

## Project structure

- `genz_consultant.py` — app launcher
- `server.py` — local static-file web server
- `index.html` — main page
- `style.css` — layout and styling
- `script.js` — chat behavior and random responses