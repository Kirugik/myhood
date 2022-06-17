from django import forms
from django.contrib.auth.models import User
from .models import Profile, Hood, Business, Update


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'hood', 'created')  