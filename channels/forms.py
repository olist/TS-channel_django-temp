from django.forms import ModelForm

from channels.models import Marketplace


class MarketplaceForm(ModelForm):
    class Meta:
        model = Marketplace
        fields = ["name"]
