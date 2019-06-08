# -*- coding: utf-8 -*-
from flask_pymongo import PyMongo
from webargs.flaskparser import FlaskParser
from apscheduler.schedulers.background import BackgroundScheduler


mongo = PyMongo()
parser = FlaskParser()
scheduler = BackgroundScheduler()

