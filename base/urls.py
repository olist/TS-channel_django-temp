from django.urls import path

from . import views

urlpatterns = [
    path('', views.base_template, name='base_template'),
]
