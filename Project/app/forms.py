from django import forms
from .models import *

class ContactForm(forms.Form):
    full_name = forms.CharField(label="Your name",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'full_name'
    }))

    email = forms.EmailField(label="Your email",widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'email'
    }))

    subject = forms.CharField(label="Your subject",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'subject'
    }))

    message = forms.CharField(label="Your message",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'message'
    }))
