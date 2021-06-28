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
def test_deve_retornar_400_quando_acessar_rota_marketplace_create_sem_dados_form(client):
    url_test = reverse("marketplace_create")
    res = client.post(url_test)
    assert res.status_code == 400


@pytest.mark.django_db
def test_deve_retornar_200_quando_acessar_rota_marketplace_update(client):
    data = {
        "name": "teste rota"
    }
    url_test = reverse("marketplace_update", kwargs={'id': 1})
    res = client.patch(url_test, data=data)
    assert res.status_code == 200


@pytest.mark.django_db
def test_deve_retornar_200_quando_acessar_rota_marketplace_delete(client):
    url_test = reverse("marketplace_delete", kwargs={'id': 1})
    res = client.delete(url_test)
    assert res.status_code == 400
