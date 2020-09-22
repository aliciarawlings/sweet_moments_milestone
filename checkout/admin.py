from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('order_item_total')


class OrderAdmin(admin.ModelAdmin):
    order_inline = (OrderItemAdmin)
    order_info = ('order_number',
                  'date', 'delivery_cost',
                 'order_total', 'grand_total',
                 )


list_display =('order_number',
 'date', 'fullname',
  'grand_total')


ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
