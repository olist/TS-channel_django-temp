from django.forms import ModelForm
from channels.models import ProductPost, Marketplace

class ProductPostForm(ModelForm):
    class Meta:
        model = ProductPost
        fields = '__all__'



class MarketplaceForm(ModelForm):
    class Meta:
        model = Marketplace
        fields = ["name"]
