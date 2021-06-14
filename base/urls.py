from django.urls import path
from django.contrib.auth import views as auth_views
from base.views import *

urlpatterns = [
    path('', base_template, name='base_template'),
    path('register/', become_user, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
]
