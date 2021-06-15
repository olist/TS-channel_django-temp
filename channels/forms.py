from django.forms import ModelForm
from channels.models import ProductPost


class ProductPostForm(ModelForm):
    class Meta:
        model = ProductPost
        fields = "__all__"
