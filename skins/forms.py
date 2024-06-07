from django import forms
from .models import Skin

class SkinForm(forms.ModelForm):
    class Meta:
        model = Skin
        fields = ['name', 'price', 'url_image']