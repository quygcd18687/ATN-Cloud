from django import forms
from .models import Toys
class ToyCreate(forms.ModelForm):
    class Meta:
        model = Toys
        fields = '__all__'