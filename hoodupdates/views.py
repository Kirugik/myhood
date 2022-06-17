from django.shortcuts import render, redirect
from .models import Profile, Hood, Business, Update

# Create your views here.
def index(request):
    hoods = Hood.objects.all()
    
    context = {'hoods': hoods}
    return render(request, 'index.html', context)
