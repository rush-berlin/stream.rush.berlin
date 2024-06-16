import flask
from flask_cors import CORS

import frontend
import api

import logging
logging.basicConfig(level=logging.DEBUG)

web = flask.Flask(__name__)

# init CORS
cors = CORS(web, resources={"*": {"origins": ["https://rush.berlin"]}})
cors.init_app(web)

web.register_blueprint(api.api)
web.register_blueprint(frontend.frontend)
