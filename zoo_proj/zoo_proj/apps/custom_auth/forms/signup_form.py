from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(label='Email', max_length=50)
    last_name = forms.CharField(label='Apellido', max_length=50)