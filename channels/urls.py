from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_product, name="list-products"),
    path("new/", views.create_product, name="create-product"),
    path("update/<post_id>", views.update_product, name="update-product"),
    path("delete/<post_id>", views.delete_product, name="delete-product"),
    path("marketplace", views.list_marketplace, name="list-marketplace"),
    path("marketplace/new", views.add_marketplace, name="create-marketplace"),
    path(
        "marketplace/update/<mkt_id>",
        views.update_marketplace,
        name="update-marketplace",
    ),
    path(
        "marketplace/delete/<mkt_id>",
        views.delete_marketplace,
        name="delete-marketplace",
    ),
    path("marketplace_api/", views.marketplace_api, name="marketplace_api"),
    path(
        "marketplace_api/list", views.marketplace_list, name="marketplace_list"
    ),
    path(
        "marketplace_api/create",
        views.marketplace_create,
        name="marketplace_create",
    ),
    path(
        "marketplace_api/update/<str:id>/",
        views.marketplace_update,
        name="marketplace_update",
    ),
    path(
        "marketplace_api/delete/<str:id>/",
        views.marketplace_delete,
        name="marketplace_delete",
    ),
    path("product_post_api/", views.product_post_api, name="product_post_api"),
    path(
        "product_post_api/list",
        views.product_post_list,
        name="product_post_list",
    ),
    path(
        "product_post_api/create",
        views.product_post_create,
        name="product_post_create",
    ),
    path(
        "product_post_api/update/<str:id>/",
        views.product_post_update,
        name="product_post_update",
    ),
    path(
        "product_post_api/delete/<str:id>/",
        views.product_post_delete,
        name="product_post_delete",
    ),
]
