#!/usr/bin/env python3

# imports
import flask
import urllib
from zomstream import Zomstream

streamList = []
zomstream = Zomstream()

frontend = flask.Blueprint('frontend', __name__)

@frontend.route("/")
def start():
    playerTemplate = '%s/player.html.j2' % zomstream.configuration['template_folder']
    page = flask.render_template(
        playerTemplate, 
        streamname='stream',
        appname='live',
        configuration=zomstream.configuration
        )
    return page
