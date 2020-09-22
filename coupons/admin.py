from django.contrib import admin
from .models import Coupon


class CouponAdmin(admin.ModelAdmin):
    list_display =['discount_code', 'start_date', 'end_date', 'discount', 'valid']
    list_filter = ['valid', 'start_date', 'end_date']
    search = ['discount_code']


admin.site.register(Coupon, CouponAdmin)

    