from html.entities import html5
import unittest
from main import create_app
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["FLASK_ENV"] = "testing" 

class TestPosts(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_post_index(self):
        response = self.client.get("/feed/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Feed</h2>', response.data)

    def test_create_bad_post(self):
        response = self.client.post("/submit_post/", data={"post_title": ""})
        self.assertEqual(response.status_code, 400)