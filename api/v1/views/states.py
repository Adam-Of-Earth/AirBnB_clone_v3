#!/bin/python3
"""creates a flask route that returns json status"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger import Swagger, swag_from
from models import storage

@app_views.route('/states', strict
