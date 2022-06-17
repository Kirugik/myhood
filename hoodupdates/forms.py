from django import forms
from django.contrib.auth.models import User
from .models import Profile, Hood, Business, Update


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'hood', 'created')  


class CreateHoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = ('hood_admin', 'since')


class PostBusinessForm(forms.ModelForm): 
    class Meta:
        model = Business
        exclude = ('business_owner', 'location', 'date_started') 


class NewUpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        exclude = ('user', 'hood', 'posted') 