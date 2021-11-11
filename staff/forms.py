from django import forms
from store.models import Product


class NewProduct(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []
