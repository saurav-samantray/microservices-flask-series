# app.py
from datetime import datetime
import logging
import time
import json
import os

from flask import Flask
from flask import request, send_from_directory, jsonify, Flask, render_template, redirect, url_for, abort, make_response
from config import BaseConfig
from celery import Celery
from celery.result import AsyncResult
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config.from_object(BaseConfig)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'],backend=app.config['CELERY_RESULT_BACKEND'])
#celery.conf.update(app.config)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_files():
    app.logger.info("Recieved request for uploading a file")
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    task = long_task.delay(filename)
    return make_response(jsonify({"task_id":task.id,"success":True}), 200)

@app.route('/upload/<task_id>')
def upload(task_id):
    res = AsyncResult(task_id)
    app.logger.info(res)
    return make_response(jsonify({"task_id":task_id,"status":res.status}), 200)

@app.route('/download/<filename>')
def download(filename):
    app.logger.info("Received request for file download")
    return send_from_directory(app.config['DOWNLOAD_PATH'], filename)



@celery.task(name='long.processing.task')
def long_task(filename):
    app.logger.info('This is being processed from celery')
    processed_file = open(os.path.join(app.config['DOWNLOAD_PATH'])+"/"+filename, 'w') 
    with open(app.config['UPLOAD_PATH']+"/"+filename, "r") as file:
        for line in file.readlines():
            app.logger.info(line.rstrip())
            processed_file.write(line.rstrip())
    processed_file.close() 
    time.sleep(5)

if __name__ == '__main__':
    app.run(debug=True)
