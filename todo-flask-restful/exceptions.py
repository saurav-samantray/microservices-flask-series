from werkzeug.exceptions import HTTPException

class ToDoAlreadyExists(HTTPException):
    pass