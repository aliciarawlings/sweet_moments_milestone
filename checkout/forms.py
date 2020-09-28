from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta: 
        model = Order
        template_name = 'checkout/checkout.html'
        fields = ('first_name', 'second_name', 'email', 'address_1', 'address_2', 'country', 'county', 'telephone')
        
        
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)