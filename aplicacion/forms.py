from django import forms

class productForm(forms.Form):
    product_name = forms.CharField(max_length=50, required=True)
    product_price = forms.CharField(required=True)