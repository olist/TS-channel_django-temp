from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class ProductPost(models.Model):

    marketplace = models.ForeignKey('Marketplace', models.DO_NOTHING, related_name='posted_products')
    product_catalog_id = models.IntegerField(default=0)                                             # Seria uma relação com catalog
    seller_id = models.IntegerField(default=0)                                                      # Seria uma relação com sellers
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'ProductPost'