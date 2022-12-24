from django import forms

class ServerForm(forms.Form):
    server_id = forms.CharField(max_length=10, min_length=4)
    secret_key = forms.CharField(max_length=20, min_length=4, widget=forms.PasswordInput())
    secret_key_cnf = forms.CharField(max_length=20, min_length=4, widget=forms.PasswordInput())
