#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import make_response
from flask import render_template

blueprint = Blueprint('dashboard', __name__)

@blueprint.route('/')
def hello():
    """Returns the landing page."""
    return render_template('index.html')

@blueprint.route('/more')
def more():
    return render_template('more.html')