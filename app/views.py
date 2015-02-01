from app import app, mongo
from flask import render_template, redirect, url_for, flash, make_response, request, session

@app.route('/')
def index():
    test = mongo.db.entity.find({'test': "complete"})
    print test[0]
    return render_template('base.html', test=test)

