import unittest
from app import app, db, init_db
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        init_db(app)
        with app.app_context():
            user_1 = User(id="1", name="Juan Diego", age=30, email="j.garcia55@uniandes.edu.co")
            db.session.add(user_1)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_local_user_should_be_equal_to_data(self):
        user_1 = User(id="1", name="Juan", age=30, email="j.garcia55@uniandes.edu.co")
        self.assertEqual(user_1.name, "Juan")
        self.assertEqual(user_1.email, "j.garcia55@uniandes.edu.co")
        self.assertEqual(user_1.age, 30)

    def test_update_user_should_return_200(self):
        response = self.client.get('/users/update')
        self.assertEqual(response.get_data(as_text=True), "Este es una ruta para actualizar usuarios")
        self.assertEqual(response.status_code, 200)

    def test_get_users_should_return_201(self):
        response = self.client.get('/users/')
        self.assertEqual(response.get_json()["users"], "Juan Diego")