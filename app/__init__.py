from flask import flask
from config import config_options

def create_app(config_name):
    '''
    Function that takes configuration setting key as an argument

    Args:
        config_name: name of the configuration to be used
    '''

    # Initializing application
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    return app