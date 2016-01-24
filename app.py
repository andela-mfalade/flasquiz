import os

from flask import Flask
from flask import url_for

import app_routes

app = Flask(__name__)
app_routes.router(app)

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = os.environ.get('SERVER_PORT', 5555)
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
