from django.shortcuts import redirect, reverse
from .forms import AddCouponForm
from .models import Coupon
from django.utils import timezone


def apply_coupon(request):
    now = timezone.now()
    form = AddCouponForm(request.POST)
    if form.is_valid():
        discount_code = form.cleaned_data['discount_code']
        try:
            coupon = Coupon.objects.get(discount_code__iexact=discount_code,
                                        start_date__lte=now,
                                        end_date__gte=now,
                                        valid=True)
            request.session['coupon'] = {
                "discount_code": coupon.discount_code,
                "discount": coupon.discount
            }

        except Coupon.DoesNotExist:
            request.session['coupon'] = None
    return redirect(reverse('checkout'))
