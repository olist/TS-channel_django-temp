from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_product, name="list-products"),
    path("new/", views.create_product, name="create-product"),
    path("update/<post_id>", views.update_product, name="update-product"),
    path("delete/<post_id>", views.delete_product, name="delete-product"),
    path("marketplace", views.list_marketplace, name='list-marketplace'),
    path("marketplace/new", views.add_marketplace, name='create-marketplace'),
    path("marketplace/update/<mkt_id>", views.update_marketplace,
         name='update-marketplace'),
    path("marketplace/delete/<mkt_id>", views.delete_marketplace,
         name='delete-marketplace'),
]
