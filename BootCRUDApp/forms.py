from django import forms

from .models import GarbageModel


class GarbageForm(forms.ModelForm):
    class Meta:
        model = GarbageModel
        fields = '__all__'