from django.test import TestCase

# Create your tests here.


class TestBase(TestCase):
    def setUp(self):
        self.register_account = {
            "email": "test@gmail.com",
            "password": "testpass",
            "username": "teste",
        }
        self.login_user = {
            "username": "teste",
            "password": "testpass",
        }

    def test_register_user(self):
        res = self.client.post("/register/", self.register_account)
        self.assertEqual(res.status_code, 200)

    def test_login_user(self):
        res = self.client.post("/login/", self.login_user)
        self.assertEqual(res.status_code, 200)
