from django.shortcuts import render, redirect
from django.http.response import Http404 
from .models import Profile, Hood, Business, Update
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UpdateProfileForm, CreateHoodForm, PostBusinessForm, NewUpdateForm
from django.core.exceptions import ObjectDoesNotExist 

# Create your views here.
def index(request):
    hoods = Hood.objects.all()
    
    context = {'hoods': hoods}
    return render(request, 'index.html', context)



def profile(request, username):
    user = User.objects.get(username=username)

    try:
        profile = Profile.objects.get(user=user.id)
    except ObjectDoesNotExist:
        raise Http404()
        
    businesses = Business.objects.filter(business_owner = profile)
    updates = Update.objects.filter(user = profile)


    context = {'user': user, 'profile': profile, 'businesses': businesses, 'updates': updates}
    return render(request, 'hood/profile.html', context)


def update_profile(request, username):
    user = User.objects.get(username = username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance = request.user.profile)
    
    context = {'form': form}
    return render(request, 'hood/update_profile.html', context)



def create_hood(request):
    if request.method == 'POST':
        form = CreateHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.hood_admin = request.user.profile
            hood.save()
            return redirect('index')
    else:
        form = CreateHoodForm()

    context = {'form': form}
    return render(request, 'hood/create_hood.html', context)


def view_hood(request, hood_id):
    hood = Hood.objects.get(id=hood_id)
    businesses = Business.objects.filter(hood = hood)
    updates = Update.objects.filter(hood = hood) 
    updates = updates[::-1] 

    context = {'hood': hood, 'businesses': businesses, 'updates': updates}
    return render(request, 'hood/view_hood.html', context)



def post_a_business(request):
    pass 

def create_hood_update(request):
    pass 
