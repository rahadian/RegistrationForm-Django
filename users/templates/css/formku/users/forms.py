from django.contrib.auth.forms import AuthenticationForm
from django import forms
#from phonenumber_field.modelfields import PhoneNumberField
class UserForm(forms.Form):
        nama = forms.CharField(max_length=100)
        email = forms.EmailField()
        phone = forms.CharField(max_length=15)
        pekerjaan= forms.CharField(max_length=100)
        institusi = forms.CharField(max_length=100)

#class LoginForm(AuthenticationForm):
#	username = forms.Charfield(label="Username", max_length=30,
#					widget=forms.TextInput(attrs('class': 'form-control', 'name': 'username')))
#	password = forms.Charfield(label="Password", max_length=30,
#					widget=forms.TextInput(attrs('class': 'form-control', 'name': 'password')))

