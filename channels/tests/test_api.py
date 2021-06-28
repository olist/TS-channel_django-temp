from django.test.client import Client
from django.urls import reverse

from rest_framework.test import APIRequestFactory

import pytest

from channels.models import Marketplace, ProductPost
from channels.views import marketplace_update


@pytest.fixture
def instance_marketplace() -> Marketplace:
    marketplace = Marketplace.objects.create(name="teste")
    return marketplace


@pytest.fixture
def instance_productpost():
    marketplace = ProductPost()
    return marketplace


@pytest.mark.django_db
def test_deve_retornar_200_quando_acessar_rota_marketplace_api(client):
    url_test = reverse("marketplace_api")
    res = client.get(url_test)
    assert res.status_code == 200


@pytest.mark.django_db
def test_deve_retornar_200_quando_acessar_rota_marketplace_list(client):
    url_test = reverse("marketplace_list")
    res = client.get(url_test)
    assert res.status_code == 200


@pytest.mark.django_db
def test_deve_retornar_400_quando_acessar_rota_marketplace_create_sem_dados_form(
    client,
):
    url_test = reverse("marketplace_create")
    res = client.post(url_test)
    assert res.status_code == 400


# @pytest.mark.django_db
# def test_deve_retornar_200_quando_acessar_rota_marketplace_update(
#     client, instance_marketplace
# ):
#     instance_marketplace.save()
#     # data = {"name": "teste rota"}
#     url_test = reverse("marketplace_update", kwargs={"id": instance_marketplace.id})
#     res = client.patch(url_test)
#     assert res.status_code == 200


@pytest.mark.django_db
def test_deve_retornar_200_quando_acessar_rota_marketplace_update(
    client, instance_marketplace
):
    instance_marketplace.save()
    factory = APIRequestFactory()
    request = factory.patch(
        f"/post-products/product_post_api/update/{instance_marketplace}/",
        {"name": "oi"},
    )
    response = marketplace_update(request)
    # self.assertEqual(response.status_code, 200)
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_deve_retornar_200_quando_acessar_rota_marketplace_delete(client):
#     url_test = reverse("marketplace_delete", kwargs={"id": 1})
#     res = client.delete(url_test)
#     assert res.status_code == 400
