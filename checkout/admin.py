from django.contrib import admin
from .models import Order, OrderItem


class OrderItem(admin.TabularInline):
    model = OrderItem
    readonly = ()


class OrderAdmin(admin.ModelAdmin):
    order_info = ('order_number',
    'date', 'delivery_cost',
    'order_total', 'grand_total',
    )


list_display =('order_number',
 'date', 'fullname',
  'grand_total')


ordering = ('-date',)


