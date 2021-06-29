from django.urls import reverse
from channels.models import Marketplace, ProductPost
import pytest


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


@pytest.mark.django_db
def test_deve_retornar_201_quando_acessar_rota_marketplace_create(client):
    data = {"name": "Marketplace Teste criado"}
    url_test = reverse("marketplace_create")
    res = client.post(url_test, data=data)
    assert res.status_code == 201


@pytest.mark.usefixtures("instancia_marketplace")
@pytest.mark.django_db
def test_deve_retornar_200_quando_acessar_rota_marketplace_update(
    client, instancia_marketplace
):
    data = {"name": "Marketplace Teste Atualizado"}
    url_test = reverse(
        "marketplace_update", kwargs={"id": instancia_marketplace.id}
    )
    res = client.patch(url_test, data=data, content_type="application/json")
    assert res.status_code == 200


@pytest.mark.usefixtures("instancia_marketplace")
@pytest.mark.django_db
def test_deve_retornar_200_quando_acessar_rota_marketplace_delete(
    client, instancia_marketplace
):
    url_test = reverse(
        "marketplace_delete", kwargs={"id": instancia_marketplace.id}
    )
    res = client.delete(url_test)
    assert res.status_code == 200
