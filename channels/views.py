from django.shortcuts import redirect, render
from channels.models import ProductPost
from channels.forms import ProductPostForm


def list_product(request):
    posted_products = ProductPost.objects.all()
    return render(request, 'products.hmtl', {'posted_products': posted_products})


def create_product(request):
    post_form = ProductPostForm(request.POST or None)

    if post_form.is_valid():
        post_form.save()

        return redirect('list-products')
    
    return render(request, 'new/', {'post': post_form})


def update_product(request, post_id):
    post_product = ProductPost.objects.get(id=post_id)
    post_form = ProductPostForm(request.POST or None, instance=post_product)

    if post_form.is_valid():
        post_form.save()

        return redirect('list-products')
    
    return render(request, 'new/', {'post': post_form})


def delete_product(request, post_id):
    ProductPost.objects.get(id=post_id).delete()
    return redirect('list-products')
