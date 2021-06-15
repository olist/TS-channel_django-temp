from django.db import models


class OrderLog(models.Model):

    requested_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class ShippingLog(models.Model):

    requested_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)