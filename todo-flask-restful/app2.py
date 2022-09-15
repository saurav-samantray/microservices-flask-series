from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todoData = [
    {"id": 1, "name": "File ITR", "status": "STARTED"}, 
    {"id": 2, "name": "Complete Flask microservices", "status": "NEW"},
]

class ToDo(Resource):
	def __init__(self):
		pass

	def get(self):
		return todoData

api.add_resource(ToDo, '/api/todos')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)