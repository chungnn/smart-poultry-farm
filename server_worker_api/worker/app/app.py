# -*- coding: utf-8 -*-
from flask import Flask, request
import os
import sys
from . import DEFAULT_CLASS_NAME, DEFAULT_FILE_NAME, load_module
import logging
from logging.handlers import RotatingFileHandler
from werkzeug.exceptions import default_exceptions
from exception import api_error_handler
from extensions import mongo
from schedule import configure_scheduler



def create_app(config=None):
    """
    create Flask app
    :param config:
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(config)
    return app


def configure_app(app, filename=DEFAULT_FILE_NAME, config_class=DEFAULT_CLASS_NAME):
    """
    config app
    :param app:
    :param filename:
    :param config_class:
    :return:
    """

    # load config app
    if not os.path.isfile(filename):
        filename = DEFAULT_FILE_NAME

    # load module config
    config = load_module(filename)
    app.config.from_object(getattr(config, config_class))

    # correct log folder
    app.config['LOG_FOLDER'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logs')
    config.make_dir(app.config['LOG_FOLDER'])

    config_extension(app)
    config_log_handler(app)
    config_error_handler(app)
    configure_scheduler(app)


def config_extension(app):
    """
    init extension for app
    :return:
    """
    mongo.init_app(app)
    # jwt.init_app(app)


def config_log_handler(app):
    """
    config logger for app
    :param app:
    :return:
    """
    fmt = '%(asctime)s %(levelname)s: %(message)s [in %(funcName)s:%(pathname)s:%(lineno)d]'
    formatter = logging.Formatter(fmt)

    # info log
    info_log = os.path.join(app.config['LOG_FOLDER'], app.config['INFO_LOG'])
    info_file_handler = logging.handlers.RotatingFileHandler(info_log, maxBytes=100000, backupCount=10)
    info_file_handler.setLevel(logging.DEBUG)
    info_file_handler.setFormatter(formatter)
    app.logger.addHandler(info_file_handler)

    # error log
    error_log = os.path.join(app.config['LOG_FOLDER'], app.config['INFO_LOG'])
    error_file_handler = logging.handlers.RotatingFileHandler(error_log, maxBytes=100000, backupCount=10)
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)

    handler_console = logging.StreamHandler(stream=sys.stdout)
    handler_console.setFormatter(formatter)
    handler_console.setLevel(logging.INFO)
    app.logger.addHandler(handler_console)

    # set proper log level
    app.logger.setLevel(logging.DEBUG if app.debug else logging.ERROR)

    # unify log format for all handlers
    for h in app.logger.handlers:
        h.setFormatter(formatter)

    app.logger.info('Config filename: {0}'.format(app.config['FILE_NAME']))
    app.logger.info('App log folder: {0}'.format(app.config['LOG_FOLDER']))


def config_error_handler(app):
    """Configures the error handlers."""
    for exception in default_exceptions:
        app.register_error_handler(exception, api_error_handler)
    app.register_error_handler(Exception, api_error_handler)
