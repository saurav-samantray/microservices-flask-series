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
		return todoData, 201

	def put(self):
		todo = request.json
		for idx, td in enumerate(todoData):
			if str(td['id']) == str(todo['id']):
				todoData[idx] = todo
		return todoData

	def delete(self):
		for idx, td in enumerate(todoData):
			if str(td['id']) == str(request.args['id']):
				todoData.pop(idx)
				return {'message': 'Deleted', 'id': td['id']}

api.add_resource(ToDo, '/api/todos')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)