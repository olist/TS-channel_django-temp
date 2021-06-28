from channels.serializers import MarketplaceSerializer
from rest_framework import viewsets

from channels.models import Marketplace


class MarketplaceViewSet(viewsets.ModelViewSet):
    serializer_class = MarketplaceSerializer
    queryset = Marketplace.objects.all()
