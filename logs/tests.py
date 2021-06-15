import pytest
from .models import OrderLog, ShippingLog

# Create your tests here.
@pytest.mark.django_db
def test_order_log_model():
    order_log = OrderLog.objects.create(status="requested")
    order_log.save()
    order_response = "responsed"
    order_log.status = order_response
    assert order_log.status == "responsed"

@pytest.mark.django_db
def test_shipping_log_model():
    shipping_log = ShippingLog.objects.create(status="requested")
    shipping_log.save()
    shipping_response = "responsed"
    shipping_log.status = shipping_response
    assert shipping_log.status == "responsed"