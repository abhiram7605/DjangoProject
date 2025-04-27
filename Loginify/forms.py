from django import forms
from . import models

class UDform(forms.ModelForm):
    class Meta:
        model = models.UserDetails
        fields= "__all__"


