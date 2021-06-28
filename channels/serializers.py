from django.db.models import fields
from rest_framework import serializers
from channels.models import Marketplace, ProductPost


class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketplace
        fields = "__all__"


class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPost
        fields = "__all__"
