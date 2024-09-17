# from django.core import validators
from django import forms
from .models import User

class studentregistration(forms.ModelForm):
 class meta:
    model = User 
    field=['name','email','password']