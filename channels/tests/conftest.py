import pytest

from channels.models import Marketplace, ProductPost


@pytest.fixture
def instancia_marketplace():
    return Marketplace.objects.create(name="test")


@pytest.fixture
def instancia_product_post(instancia_marketplace):
    # {
    # "marketplace": 1,
    # "product_catalog_id": 1,
    # "seller_id": 1,
    # "status": true
    # }
    return ProductPost.objects.create(
        marketplace=instancia_marketplace.id,
        product_catalog_id=1,
        seller_id=1,
        status=True,
    )
