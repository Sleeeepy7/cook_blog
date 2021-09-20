from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
