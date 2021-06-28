from django.test.client import Client
from django.urls import reverse
import pytest


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
def test_deve_retornar_200_quando_acessar_rota_marketplace_create(client):
    url_test = reverse("marketplace_create")
    res = client.get(url_test)
    assert res.status_code == 200


@pytest.mark.django_db
def test_deve_retornar_200_quando_acessar_rota_marketplace_update(client):
    url_test = reverse("marketplace_update")
    res = client.get(url_test)
    assert res.status_code == 200


@pytest.mark.django_db
def test_deve_retornar_200_quando_acessar_rota_marketplace_delete(client):
    url_test = reverse("marketplace_delete")
    res = client.get(url_test)
    assert res.status_code == 200
