import os
from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.mail import Mail


app = Flask(__name__)
app.config.from_object('config')

mail = Mail(app)

app.config['MONGO_DBNAME'] = 'TrainingPortal'
mongo = PyMongo(app, config_prefix='MONGO')

from app import views
