from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_product, name="list-products"),
    path("new/", views.create_product, name="create-product"),
    path("update/<post_id>", views.update_product, name="update-product"),
    path("delete/<post_id>", views.delete_product, name="delete-product"),
    path("marketplace", views.add_marketplace, name='marketplace'),
    path("list-mtk", views.list_marketplace, name='list-mkt'),
    path("update-mkt/<mkt_id>", views.update_mkt, name='update-mkt'),
    path('delete-mkt/<mkt_id>', views.delete_mkt, name='delete-marketplace'),
]
