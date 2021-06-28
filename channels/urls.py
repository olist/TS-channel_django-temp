from rest_framework import urlpatterns
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from channels.views import MarketplaceViewSet
from django.urls import path

router = DefaultRouter()

router.register('marketplace', MarketplaceViewSet, basename='marketplace')

urlpatterns = router.urls
