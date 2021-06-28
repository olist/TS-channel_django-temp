from django.db.models import fields
from rest_framework import serializers
from channels.models import Marketplace


class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketplace
        fields = '__all__'