from flask import Flask, request
from flask_restful import Resource, Api
from exceptions import ToDoAlreadyExists


errors = {
    'ToDoAlreadyExists': {
        'message': "A todo with that name already exists.",
        'status': 400,
    },
}

app = Flask(__name__)
api = Api(app, errors=errors)

todoData = [
    {"id": 1, "name": "File ITR", "status": "STARTED"}, 
    {"id": 2, "name": "Complete Flask microservices", "status": "NEW"},
]

class ToDo(Resource):
	def __init__(self):
		pass

	def get(self):
		return todoData

	def post(self):
		todo = request.json
		for td in todoData:
			if td['name'] == todo['name']:
				raise ToDoAlreadyExists
		todoData.append(todo)        
		return todoData, 201

	def put(self):
		todo = request.json
		for idx, td in enumerate(todoData):
			if str(td['id']) == str(request.args['id']):
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