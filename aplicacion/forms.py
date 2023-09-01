from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class productForm(forms.Form):
    product_name = forms.CharField(max_length=50, required=True)
    product_price = forms.CharField(required=True)


class customerForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True)


class sellerForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50, required=True)
    password = forms.CharField(label="Password", max_length=50, required=True)


class UserRegistryForm(UserCreationForm):
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Name", max_length=50, required=False)
    last_name = forms.CharField(label="Last name", max_length=50, required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']


class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
