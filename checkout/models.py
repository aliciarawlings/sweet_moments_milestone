from django.conf import settings
from django.db.models import Sum
from products.models import Products
from coupons.models import Coupon
from django.db import models
from profiles.models import UserPage
import uuid


class Order(models.Model):
    order_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    coupon = models.ForeignKey(Coupon, null=True, blank=True,on_delete= models.CASCADE)
    user = models.ForeignKey(UserPage, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    first_name = models.CharField(max_length=20,null=False, blank=False)
    second_name = models.CharField(max_length=20, null=False, blank=False)
    status = models.BooleanField(default=False)
    email = models.EmailField(max_length=32, null=False)
    telephone = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=40, null=False, blank=False)
    address_1 = models.CharField(max_length=300, null=False, blank=False)
    address_2 = models.CharField(max_length=300, null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(editable=False, max_digits=10, decimal_places=2, null= False, default=0)


def calculate_total(self):
    self.grand_total = self.orderitems.aggregate(Sum('order_item_total'))['order_item_total__sum'] or 0
    self.order_total = self.grand_total
    self.save()


def save(self, *args, **kwargs):
    if not self.order_number:
        self.order_number = uuid.uuid4()
    super().save(*args, **kwargs)


def __str__(self):
    return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,on_delete= models.CASCADE, related_name='orderitems')
    products = models.ForeignKey(Products, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    order_item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank= False)

    def save(self, *args, **kwargs):
        self.order_item_total = self.products.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.products.name} on order{self.order.order_number}'






