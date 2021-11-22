# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import logging

from flask import Flask, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler
from os import path
from flask_cors import CORS

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
login_manager = LoginManager()


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    mods = [('storeman')]
    for module_name in mods:
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    flask_bcrypt.init_app(app)
    return app
