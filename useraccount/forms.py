from django import forms
from useraccount.models import UserAccount

from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=32,
    )
    password = forms.CharField(
        widget=forms.widgets.PasswordInput,
        max_length=128,
    )

class SignupForm(forms.ModelForm):
    
    class Meta:
        model = UserAccount
        fields = (
            'username',
            'password',
        )
    
    password = forms.CharField(
        widget=forms.widgets.PasswordInput,
        max_length=128,
    )
