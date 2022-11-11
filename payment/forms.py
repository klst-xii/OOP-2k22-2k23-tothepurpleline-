from django import forms
from payment.models import BillingAddress

class BillingAddressForm(forms.ModelForm):
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    zipcode = forms.CharField(label='Zip Code', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = BillingAddress
        fields = ['address', 'zipcode', 'city', 'country']