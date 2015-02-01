import os
from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.mail import Mail
from flask.ext.login import LoginManager
from bson.objectid import ObjectId

app = Flask(__name__)
app.config.from_object('config')

mail = Mail(app)

app.config['MONGO_DBNAME'] = 'TrainingPortal'
mongo = PyMongo(app, config_prefix='MONGO')

login = LoginManager()
login.init_app(app)

@login.user_loader
def load_user(user_id):
    return mongo.db.User.find_one_or_404({'_id':ObjectId(user_id)})


from app import views, models
from models import User
