from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Nombre de usuario')
    contraseña = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
