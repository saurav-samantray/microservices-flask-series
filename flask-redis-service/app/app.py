# app.py

from flask import Flask
from flask import request, jsonify
from config import BaseConfig
from flask_caching import Cache


app = Flask(__name__)
app.config.from_object(BaseConfig)

cache = Cache(app)


@app.route('/square/<int:number>')
@cache.cached(timeout=50)
def square(number):
    app.logger.info(f"Computing the square of {number}")
    return jsonify({"computed":number*number})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)