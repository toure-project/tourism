from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import hotels


class hotelform(forms.ModelForm):
    class Meta:
        model = hotels
        fields = '__all__'
