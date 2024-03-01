from django import forms
from .models import Events

class eventform(forms.ModelForm):
    class Meta:
        model = Events
        fields = "__all__"