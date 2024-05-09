from unittest import TestCase

from app import app
from models import db, Pet
from app_long_forms import *
# Additional Testing
# from models import Pet, db, connect_db

app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sqla_intro_test4'
app.config['SQLALCHEMY_ECHO'] = False


with app.app_context():
    db.drop_all()
    db.create_all()


class PetTestCase(TestCase):
    """Tests for views for Pets."""

    def setUp(self):
        """Clean up any existing Post."""
        with app.app_context():
            with app.test_client() as client:
                db.drop_all()
                db.create_all()
                self.client = app.test_client()

    def tearDown(self):
        """Clean up any fouled transaction."""
        with app.app_context():
            with app.test_client() as client:
                db.session.rollback()

    def test_pet_add_form(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.get("/add")
                html = resp.get_data(as_text=True)
                self.assertEqual(resp.status_code, 200)
                self.assertIn('<p class="h1">Add Pet</p>', html)

    def test_pet_page(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.get("/")
                html = resp.get_data(as_text=True)
                self.assertEqual(resp.status_code, 200)
                self.assertIn('<p class="h1">Pets</p>', html)

    def test_pet_add(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.post("/add", data={
                    "name": long_text_128,
                    "species": "porcupine",
                    "photo_url": "https://via.placeholder.com/150",
                    "age": 30,
                    "notes": long_text_3677,
                    "available": True
                }, follow_redirects=True)
                html = resp.get_data(as_text=True)
                self.assertEqual(resp.status_code, 200)
                self.assertIn(long_text_128, html)
                resp = client.get("/1")
                html = resp.get_data(as_text=True)
                self.assertEqual(resp.status_code, 200)
                self.assertIn(long_text_3677, html)

                resp = client.post("/add", data={
                    "name": long_text_128,
                    "species": "Cat",
                    "photo_url": "https://via.placeholder.com/150",
                    "age": 30,
                    "notes": long_text_3677,
                    "available": True
                }, follow_redirects=True)
                html = resp.get_data(as_text=True)
                self.assertEqual(resp.status_code, 200)
                self.assertIn(long_text_128, html)

                resp = client.post("/add", data={
                    "name": long_text_128,
                    "species": "Dog",
                    "photo_url": "https://via.placeholder.com/150",
                    "age": 30,
                    "notes": long_text_3677,
                    "available": True
                }, follow_redirects=True)
                html = resp.get_data(as_text=True)
                self.assertEqual(resp.status_code, 200)
                self.assertIn(long_text_128, html)

    def test_pet_edit(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.post("/add", data={
                    "name": long_text_128,
                    "species": "porcupine",
                    "photo_url": "https://via.placeholder.com/150",
                    "age": 30,
                    "notes": long_text_3677,
                    "available": True
                }, follow_redirects=True)
                html = resp.get_data(as_text=True)
                self.assertEqual(resp.status_code, 200)
                self.assertIn(long_text_128, html)
                resp = client.post("/1", data={
                    "name": long_text_128,
                    "species": "cat",
                    "photo_url": "https://via.placeholder.com/75",
                    "age": 30,
                    "notes": long_text_64,
                    "available": True
                }, follow_redirects=True)
                html = resp.get_data(as_text=True)
                self.assertEqual(resp.status_code, 200)
                self.assertIn(long_text_64, html)
                self.assertNotIn('''
                <input class="form-check-input" id="species-0" name="species" 
                type="radio" value="dog" checked="" disabled="">''', html)
                self.assertNotIn("https://via.placeholder.com/150", html)
                self.assertNotIn(long_text_3677, html)
                self.assertIn('''value="porcupine" checked disabled''', html)
                self.assertIn("https://via.placeholder.com/75", html)

                resp = client.post("/add", data={
                    "name": long_text_128,
                    "species": "dog",
                    "photo_url": "https://via.placeholder.com/150",
                    "age": 30,
                    "notes": long_text_3677,
                    "available": True
                }, follow_redirects=True)
                html = resp.get_data(as_text=True)
                self.assertEqual(resp.status_code, 200)
                self.assertIn('''(dog) added!''', html)
                self.assertIn(long_text_128, html)
