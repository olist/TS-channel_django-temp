 from django.contrib import admin
from .models import Marketplace



@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    pass