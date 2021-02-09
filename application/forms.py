
from .models import OlevelApplication, AlevelApplication
from django import forms


class AlevelForm(forms.ModelForm):
    class Meta:
        model = AlevelApplication
        fields = '__all__'


class OlevelForm(forms.ModelForm):
    class Meta:
        model = OlevelApplication
        fields = '__all__'




