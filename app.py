#!/usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

# from me import api
from me import frontend
from me.helpers.logs import log

from flask import Flask

app = Flask(__name__)

app.wsgi_app = DispatcherMiddleware(frontend.create_app(), {
    # '/api': api.create_app()
})

if __name__ == '__main__':
    log.info('Starting system.')
    app.debug = True
    app.run()