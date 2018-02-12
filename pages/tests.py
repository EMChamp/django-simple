# pages/tests.py
from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_news_page_status_code(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_anime_page_status_code(self):
        response = self.client.get('/anime/')
        self.assertEqual(response.status_code, 200) 
