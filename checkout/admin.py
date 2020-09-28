from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('order_item_total',)
    

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)
    readonly_fields = ('order_number','date',
                'order_total')


list_display =('order_number',
 'date', 'fullname')


ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
