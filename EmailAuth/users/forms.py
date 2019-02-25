from django import forms

class LoginEmail(forms.Form):
    email = forms.EmailField()
    password = forms.CharField( widget= forms.PasswordInput())


class GoalsForm(forms.Form):

        title = forms.CharField(max_length=254)
        description = forms.CharField(widget=forms.TextInput())

