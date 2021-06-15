from django.test import TestCase
from django.contrib.auth.models import User
from base.models import UserAccount
from channels.models import Marketplace, ProductPost
import pytest

# @pytest.mark.django_db
# def test_post_product(client):
# user = UserAccount.objects.create(name='blablabla')
# url = reverse('list-products')
# client = Client()
# client.force_login(user)
# response = client.get(url)
# print('response', response)
# assert response.status_code == 200


@pytest.mark.django_db
def test_account_model():
    user = User.objects.create(
        username="teste", email="teste@teste.com", password="testpasswd"
    )
    account = UserAccount.objects.create(name="testin", created_by=user)
    account.save()
    assert account.name == "testin"


@pytest.mark.django_db
def test_marketplace_model():
    marketplace = Marketplace.objects.create(name="marketplace")
    marketplace.save()
    assert marketplace.name == "marketplace"


@pytest.mark.django_db
def test_product_post_model():
    marketplace = Marketplace.objects.create(name="marketplace")
    post_product = ProductPost.objects.create(
        marketplace=marketplace,
        product_catalog_id=1,
        seller_id=1,
    )
    post_product.save()

    assert post_product.id == 1


class TestChannels(TestCase):
    def setUp(self):
        self.register_account_to_log = {
            "email": "login@gmail.com",
            "password": "loginpasswd",
            "username": "login",
        }
        self.register_account = {
            "email": "test@gmail.com",
            "password": "testpass",
            "username": "teste",
        }
        self.login_user = {
            "username": "teste",
            "password": "testpass",
        }
        marketplace = Marketplace.objects.create(name='marketplace')
        self.product_post = {
            'marketplace': marketplace.id,
            'product_catalog_id': 1,
            'seller_id': 1,
        }
        self.edit_product_post = {
            'marketplace': marketplace.id,
            'product_catalog_id': 2,
            'seller_id': 2
        }
        user = User.objects.create(**self.register_account_to_log)
        self.client.force_login(user)

    def test_register_user(self):
        res = self.client.post("/register/", self.register_account)
        self.assertEqual(res.status_code, 200)

    def test_login_user(self):
        res = self.client.post("/login/", self.login_user)
        self.assertEqual(res.status_code, 200)

    def test_get_product_post(self):
        res = self.client.get("/post-products/")
        self.assertEqual(res.status_code, 200)

    def test_create_product_post(self):
        res = self.client.post('/post-products/new/', self.product_post)
        self.assertEqual(res.status_code, 302)

    def test_update_product_post(self):
        self.client.post('/post-products/new/', self.product_post)
        product_post = ProductPost.objects.last()
        res = self.client.post(f'/post-products/update/{product_post.id}', self.edit_product_post)
        self.assertEqual(res.status_code, 302)

    def test_delete_product_post(self):
        self.client.post('/post-products/new/', self.product_post)
        product_post = ProductPost.objects.last()
        res = self.client.post(f'/post-products/delete/{product_post.id}')
        self.assertEqual(res.status_code, 302)
