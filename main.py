import os
import webbrowser

from flask import Flask

from routes import main

app = Flask(__name__)


main(app)

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = os.environ.get('SERVER_PORT', 5555)
    except ValueError:
        PORT = 5555
    webbrowser.open('http://localhost/5555')
    app.run(HOST, PORT, debug=True)
