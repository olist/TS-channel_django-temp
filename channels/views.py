from django.shortcuts import render, redirect
from channels.forms import ProductPostForm, MarketplaceForm
from django.contrib.auth.decorators import login_required
from .models import ProductPost, Marketplace


@login_required
def list_product(request):
    posted_products = ProductPost.objects.all()
    return render(request, "channels_list.html", {"posted_products": posted_products})


@login_required
def create_product(request):
    post_form = ProductPostForm(request.POST or None)

    if post_form.is_valid():
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


@login_required
def add_marketplace(request):
    if request.method == "POST":
        form = MarketplaceForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect("list-marketplace")
    else:
        form = MarketplaceForm()
    return render(request, "marketplace_form.html", {"form": form})


@login_required
def list_marketplace(request):
    list_mkt = Marketplace.objects.all()
    return render(request, "mkt_list.html", {"list_mkt": list_mkt})


@login_required
def update_marketplace(request, mkt_id):
    mkt = Marketplace.objects.get(id=mkt_id)
    post_form = MarketplaceForm(request.POST or None, instance=mkt)

    if post_form.is_valid():
        post_form.save()

        return redirect("list-marketplace")
    return render(request, "marketplace_form.html", {"form": post_form})


@login_required
def delete_marketplace(request, mkt_id):
    Marketplace.objects.get(id=mkt_id).delete()
    return redirect("list-marketplace")
