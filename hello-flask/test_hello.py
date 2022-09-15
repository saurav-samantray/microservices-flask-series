import unittest
import json

import app

BASE_URL = 'http://localhost:5000'

class TestHelloApi(unittest.TestCase):
    
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_hello(self):
        response = self.app.get(BASE_URL)
        #data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main() 