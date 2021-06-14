from django.shortcuts import render
from channels.models import ProductPost


def list_product(request):
    posted_products = ProductPost.objects.all()
    return render(request, 'products.hmtl', {'posted_products': posted_products})


def create_product(request):
    pass


def update_product(request):
    pass


def delete_product(request):
    pass
