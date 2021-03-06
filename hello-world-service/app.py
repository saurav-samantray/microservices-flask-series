import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ.get('CONFIG_SOURCE'))


@app.route('/')
def hello():
    app.logger.debug("Hello debug")
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)