#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_assets import Environment, Bundle

# Bundle the vendors.
css_vendor = Bundle('css/vendor/normalize.css',
                    'css/vendor/bootstrap.css',
                    'css/vendor/flat-ui.css',
                    'css/vendor/odometer-theme.css',
                    filters='cssmin', output='css/vendors.min.css')

# Bundle all the CSS.
css_all = css_vendor

# Get JS vendors in order.
js_vendor = Bundle('js/vendor/jquery.backstretch.min.js',
                   filters='jsmin', output='js/vendor.min.js')

js_main = Bundle('js/main.js', filters='jsmin', output='js/main.min.js')

def init_app(app):
    webassets = Environment(app)
    webassets.register('css_vendor', css_vendor)
    webassets.register('css_all', css_all)
    webassets.register('js_vendor', js_vendor)
    # webassets.register('js_main', js_main)
    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug