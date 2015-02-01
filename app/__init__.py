import os
from flask import Flask
from flask.ext.pymongo import pyMongo
from flask.ext.mail import Mail


app = Flask(__name__)
app.config.from_object('config')

mail = Mail(app)

app.config['MONGO_DBNAME'] = 'TrainingPortal'
mongo = pyMongo(app, config_prefix='MONGO')

