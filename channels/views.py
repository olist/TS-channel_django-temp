from django.shortcuts import render, redirect
from rest_framework import serializers
from channels.forms import ProductPostForm, MarketplaceForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from channels.serializers import MarketplaceSerializer, ProductPostSerializer
from .models import ProductPost, Marketplace


@login_required
def list_product(request):
    posted_products = ProductPost.objects.all()
    return render(
        request, "channels_list.html", {"posted_products": posted_products}
    )


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


##################################################### API marketplace ############################################################
@api_view(["GET"])
def marketplace_api(resquest):
    api_urls = {
        "List": "/list",
        "Create": "/create",
        "Update": "/update",
        "Delete": "/delete",
    }
    return Response(api_urls)


@api_view(["GET"])
def marketplace_list(request):
    marketplace = Marketplace.objects.all()
    serializer = MarketplaceSerializer(marketplace, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def marketplace_create(request):
    serializer = MarketplaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["PATCH"])
def marketplace_update(request, id):
    marketplace = Marketplace.objects.get(id=id)
    serializer = MarketplaceSerializer(instance=marketplace, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def marketplace_delete(request, id):
    marketplace = Marketplace.objects.get(id=id)
    marketplace.delete()
    return Response("Marketplace deleted!")


############################################ API Productpost ###################################
@api_view(["GET"])
def product_post_api(resquest):
    api_urls = {
        "List": "/list",
        "Create": "/create",
        "Update": "/update",
        "Delete": "/delete",
    }
    return Response(api_urls)


@api_view(["GET"])
def product_post_list(request):
    productpost = ProductPost.objects.all()
    serializer = ProductPostSerializer(productpost, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def product_post_create(request):
    serializer = ProductPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["PATCH"])
def product_post_update(request, id):
    productpost = ProductPost.objects.get(id=id)
    serializer = ProductPostSerializer(instance=productpost, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def product_post_delete(request, id):
    productpost = ProductPost.objects.get(id=id)
    productpost.delete()
    return Response("Product Post deleted!")
