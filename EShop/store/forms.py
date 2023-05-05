from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User

class SignUpform(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password Again',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username','email')
        
class LogInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,'class':'form-control'}))
    password = forms.CharField(
        label= "Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'class':'form-control'}),
    )
    error_messages = {
        "invalid_login": (
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": ("This account is inactive."),
    }
class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Old password"),strip=False,
                                   widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "autofocus": True,'class':'form-control'})),
    new_password1 = forms.CharField(label=("New Password"),strip=False,
                                   widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "autofocus": True,'class':'form-control'})),
    new_password2 = forms.CharField(label=("New Password Again"),strip=False,
                                   widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "autofocus": True,'class':'form-control'}))