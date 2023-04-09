from .models import Product
from django import forms

# form


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['code', 'name', 'description', 'price', 'size']
