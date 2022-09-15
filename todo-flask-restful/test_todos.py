import unittest
import app3 as app

unittest.TestLoader.sortTestMethodsUsing = None
BASE_URL = '/api/todos'

class ToDosTest(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.app.testing = True
        self.client = self.app.test_client()

    def test_get_todos(self):
        response = self.client.get(BASE_URL)
        self.assertEqual(response.status_code, 200)

    def test_create_todos_success(self):
        response = self.client.post(BASE_URL, json = {"id": 3, "name": "Complete Python Basics", "status": "COMPLETE"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json), 3)

    def test_create_todos_error(self):
        response = self.client.post(BASE_URL, json = {"id": 3, "name": "File ITR", "status": "COMPLETE"})
        self.assertEqual(response.status_code, 400)     

if __name__ == "__main__":
    unittest.main() 