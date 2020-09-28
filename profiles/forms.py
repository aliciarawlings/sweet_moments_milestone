from django import forms
from .models import UserPage


class UserProfileForm(forms.ModelForm):
    class Meta: 
        model = UserPage
        exclude = ('user',)
        
        
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    placeholders = {
    'profile_email': profile_email ,
    'profile_telephone': profile_telephone,
    'profile_country' :profile_country,
    'profile_county': profile_county ,
    'profile_address_1 ': profile_address_1 ,
    'profile_address_2': profile_address_2,

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
