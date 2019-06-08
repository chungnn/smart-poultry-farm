# -*- coding: utf-8 -*-
from flask_pymongo import PyMongo
from webargs.flaskparser import FlaskParser
from apscheduler.schedulers.background import BlockingScheduler


mongo = PyMongo()
parser = FlaskParser()
scheduler = BlockingScheduler()

