from django import forms
from .models import UserPage


class UserProfileForm(forms.ModelForm):
    class Meta: 
        model = UserPage
        exclude = ('user',)
        
        
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    placeholders = {
    'primary_telephone': 'telephone',
    'primary_country': 'country',
    'primary_county': 'county' ,
    'primary_address_1': 'address_1 ',
    'primary_address_2':'address_2',

    }
    set.fields['profile_telephone'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if field != 'profile_country':
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder - placeholders[field]
                set.fields[field].widget.attrs['placeholder'] = placeholder
                set.fields[field].label = False
