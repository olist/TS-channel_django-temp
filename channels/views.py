from django.shortcuts import render, redirect
from channels.forms import ProductPostForm
from django.contrib.auth.decorators import login_required
from .models import ProductPost


@login_required
def list_product(request):
    posted_products = ProductPost.objects.all()
    return render(request, "channels_list.html", {"posted_products": posted_products})


@login_required
def create_product(request):
    post_form = ProductPostForm(request.POST or None)

    if post_form.is_valid():
        print("oq deu auqo", post_form)
        post_form.save()

        return redirect("list-products")
    return render(request, "channels_form.html", {"post": post_form})


@login_required
def update_product(request, post_id):
    post_product = ProductPost.objects.get(id=post_id)
    post_form = ProductPostForm(request.POST or None, instance=post_product)

    if post_form.is_valid():
        post_form.save()

        return redirect("list-products")
    return render(request, "channels_form.html", {"post": post_form})


@login_required
def delete_product(request, post_id):
    ProductPost.objects.get(id=post_id).delete()
    return redirect("list-products")
