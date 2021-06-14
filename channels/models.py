from django.db import models
from django.contrib.auth.models import User


class UserAccount(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='user',
                                      on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Marketplace(models.Model):


    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class ProductPost(models.Model):


    marketplace = models.ForeignKey(
        'Marketplace', models.DO_NOTHING, related_name='posted_products')
    product_catalog_id = models.IntegerField(default=0)                     # Seria uma relação com catalog
    seller_id = models.IntegerField(default=0)                              # Seria uma relação com sellers
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'ProductPost'
