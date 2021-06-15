from django.urls import path
from channels.views import list_product, create_product, update_product, delete_product

urlpatterns = [
    path("", list_product, name="list-products"),
    path("new/", create_product, name="create-product"),
    path("update/<post_id>", update_product, name="update-product"),
    path("delete/<post_id>", delete_product, name="delete-product"),
]
