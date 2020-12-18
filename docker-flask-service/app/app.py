# app.py
from datetime import datetime
import logging

from flask import Flask
from flask import request, jsonify, render_template, session
from config import BaseConfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(BaseConfig)

db = SQLAlchemy(app)

from models import Visit

@app.route('/')
def index():
    app.logger.info("Rendering homepage from flask server")
    counter = 0
    v = Visit.query.first()
    
    #If very first visist, create the first entry into DB,
    #which would be subsequently used by all clients
    if not v:
        v = Visit()
        db.session.add(v)
        db.session.commit()
    return render_template('index.html', counter=v.count)


@app.route('/click')
def click_counter():
    v = Visit.query.first()
    v.count +=1
    db.session.commit()
    app.logger.info("Request to increment counter. New value {v.count}")
    return jsonify({"counter":v.count})

if __name__ == '__main__':
    app.run(debug=True)
