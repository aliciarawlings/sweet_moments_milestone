from django import forms
from .models import Order
from crispy_forms.helper import FormHelper


class OrderForm(forms.Form):
    class Meta: 
        model = Order
        title = forms.TypedChoiceField(
            label= "Title",
            choices= ((1, "Mr"), (2, "Mrs"), (3, "Ms"))
        )
        label = "Order Details"
        fields = ['first_name', 'second_name', 'email', 'address_1','address_2', 'country', 'county','telephone']
        required = True
    

def __init__(self, *args, **kwargs):
    super().__inti__(*args, **kwargs)
    

    
