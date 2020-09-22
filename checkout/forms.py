from django import forms
from .models import Order


class OrderForm(forms.Form):
    class Meta: 
        model = Order
        fields = ['first name', 'second name', 'email', 'address_1','address_2', 'country', 'county','telephone']
    

def __init__(self, *args, **kwargs):
    super().__inti__(*args, **kwargs)