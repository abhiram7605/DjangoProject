from django import forms
from . import models

class UDform(forms.ModelForm):
    class Meta:
        model = models.UserDetails
        fields= "__all__"

class UDsigninform(forms.Form):
    Email = forms.EmailField(max_length=50)
    Password = forms.CharField(max_length=12)
    



