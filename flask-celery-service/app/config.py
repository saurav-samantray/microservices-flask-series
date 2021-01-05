# config.py


import os


class BaseConfig(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = True
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0')
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_REDIS_MAX_CONNECTIONS = 5
    MAX_CONTENT_LENGTH = 1024 * 1024
    UPLOAD_EXTENSIONS = ['.txt','.csv','json']
    UPLOAD_PATH = 'uploads'
    DOWNLOAD_PATH = 'download'
