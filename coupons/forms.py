from django import forms


class AddCouponForm(forms.Form):
    discount_code = forms.CharField()
