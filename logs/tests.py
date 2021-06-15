from logs.models import OrderLog, ShippingLog
import pytest


data = {
    'buyer': {
        'cpf': 11122233344,
        'email': 'teste@test.com',
    },
    'products': [
        {
            'catalog_id': 1,
            'product_post_id': 1,
            'seller_id': 1,
            'price': 5,
        }
    ]
}



@pytest.fixture
def emulate_shipping_data():
    return [ShippingLog.objects.create(status="requested")]

@pytest.fixture
def emulate_order_data():
    return [OrderLog.objects.create(status="requested")]

@pytest.mark.django_db
def test_request_order(emulate_order_data):
    order_log = emulate_order_data[0]
    __fake_request('http://localhost:3000/orders/', data, order_log.id)
    assert order_log.status == "requested"

@pytest.mark.django_db
def test_response_to_update_order(emulate_order_data, post_order_id=1, status='responsed'):
    post_order_id = emulate_order_data[0].id
    order_log = OrderLog.objects.get(id=post_order_id)
    order_log.status = status
    order_log.save()
    
    assert order_log.status == "responsed"

@pytest.mark.django_db
def test_request_shipping(emulate_shipping_data):
    shipping_log = emulate_shipping_data[0]
    __fake_request('http://localhost:3000/shipping/', data, shipping_log.id)
    assert shipping_log.status == "requested"

@pytest.mark.django_db
def test_response_to_update_shipping(emulate_shipping_data, post_ship_id=1, status='responsed'):
    post_ship_id = emulate_shipping_data[0].id
    shipping_log = ShippingLog.objects.get(id=post_ship_id)
    shipping_log.status = status
    shipping_log.save()

    assert shipping_log.status == "responsed"

def __fake_request(endpoint, data, post_id):
    return

