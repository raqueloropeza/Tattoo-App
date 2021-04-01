from django import forms 
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta: 
        model = Profile
        fields = "__all__"

class LocationForm(forms.ModelForm):
    class Meta: 
        model = Map
        fields = "__all__"
        widgets = {"user":forms.HiddenInput()}