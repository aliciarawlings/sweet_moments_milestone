from django.conf import settings
from django.db.models import Sum
from products.models import Products
from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    email = models.CharField(max_length=32, null= False, editable= False)
    telephone = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=40, null=False, blank=False)
    address_1 = models.CharField(max_length=4, null=False, blank=False)
    address_2 = models.CharField(max_length=4, null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null= False, default=0)

    
class OrderItem(models.Model):
    cart_item = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=False, blank=False, on_delete= models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    order_item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank= False)

    def __str__(self):
        return self.title



