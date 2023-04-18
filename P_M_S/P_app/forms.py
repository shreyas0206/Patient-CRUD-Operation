from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from . models import Patient

class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields =['name','age','phone','Details']
        lables = {'name':'Name','age':'Age','phone':'Phone-No'}
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'Details':forms.TextInput(attrs={'class':'form-control'}),
        }
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
