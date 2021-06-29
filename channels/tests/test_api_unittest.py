import json
from rest_framework import status
from unittest.mock import Mock, MagicMock, patch, create_autospec
from django.test import TestCase, Client
from django.urls import reverse
from channels.models import Marketplace, ProductPost
from channels.serializers import MarketplaceSerializer, ProductPostSerializer


# initialize the APIClient app
client = Client()


class GetAllMarketplaceTest(TestCase):
    def setUp(self):

        self.marketplace_valido = {
            "name": "Test 1",
        }

        self.marketplace_invalido = {
            "name": 1,
        }

    def test_deve_retornar_200_quando_request_get_em_marketplace_list(self):
        # get API response
        response = client.get(reverse("marketplace_list"))
        # get data from db
        objects = Marketplace.objects.all()
        serializer = MarketplaceSerializer(objects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllProductPostTest(TestCase):
    # @patch("channels.models.Marketplace")
    def setUp(self):
        self.marketplace = Marketplace.objects.create(name="Test 1")
        self.marketplace.save()

        self.produto_valido = {
            "marketplace": self.marketplace.id,
            "product_catalog_id": 1,
            "seller_id": 1,
            "status": True,
        }

        self.produto_invalido = {
            "marketplace": 2,
            "product_catalog_id": 2,
            "seller_id": 2,
            "status": True,
        }

    # def tearDown(self) -> None:
    #     Marketplace.objects.filter(id=self.marketplace.id).delete()

    def test_deve_retornar_200_quando_request_get_em_product_post_list(self):
        # get API response
        response = client.get(reverse("product_post_list"))
        # get data from db
        objects = ProductPost.objects.all()
        serializer = ProductPostSerializer(objects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deve_retornar_201_quando_request_post_em_product_post_create_com_produto_valido(
        self,
    ):
        response = client.post(
            reverse("product_post_create"),
            data=json.dumps(self.produto_valido),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_deve_retornar_400_quando_request_post_em_product_post_create_com_produto_invalido(
        self,
    ):
        response = client.post(
            reverse("product_post_create"),
            data=json.dumps(self.produto_invalido),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
