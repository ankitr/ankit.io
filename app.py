#/usr/bin/env python

from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/')
def hello():
    return Response('Hi, I\'m Ankit. Email me '
    '<a href="mailto:me@ankit.io">here</a>. This page is under construction.')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)