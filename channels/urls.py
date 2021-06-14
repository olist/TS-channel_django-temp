from django.contrib.auth import views as auth_views

from django.urls import path
from channels.views import *

urlpatterns = [  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
    path('register/', become_user, name='register')
    path("", list_product, name="list-products"),
    path("new/", create_product, name="create-product"),
    path("update/<post_id>", update_product, name="update-product"),
    path("delete/<post_id>", delete_product, name="delete-product"),
]
