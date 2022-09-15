from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todoData = [
    {"id": 1, "name": "File ITR", "status": "STARTED"}, 
    {"id": 2, "name": "Complete Flask microservices", "status": "NEW"},
]

class ToDo(Resource):
	def get(self):
		return todoData
	def post(self):
		todo = request.json
		todoData.append(todo)
		return todoData		

api.add_resource(ToDo, '/api/todos')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)