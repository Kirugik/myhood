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


def sign_up(request):
    return render(request, 'auth/sign_up.html') 


def sign_in(request):
    return render(request, 'auth/sign_in.html') 


def sign_out(request):
    pass 



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



def post_a_business(request, hood_id):
    if request.method == 'POST':
        hood = Hood.objects.get(id =hood_id)
        form = PostBusinessForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_business_form = form.save(commit=False)
            new_business_form.hood = hood
            new_business_form.business_owner = request.user.profile
            new_business_form.create_business()
            return redirect('view-hood', hood.id)
    else:
        form = PostBusinessForm()
    
    context = {'form': form}
    return render(request, 'hood/post_business.html', context) 



def create_hood_update(request, hood_id):
    hood = Hood.objects.get(id =hood_id)

    if request.method == 'POST':
        form = NewUpdateForm(request.POST)
        if form.is_valid():
            new_hood_update = form.save(commit=False)
            new_hood_update.hood = hood
            new_hood_update.user = request.user.profile
            new_hood_update.save()
            return redirect('view-hood', hood.id)
    else:
        form = NewUpdateForm()

    context = {'form': form}
    return render(request, 'hood/create_update.html', context)



def join_hood(request, id):
    try:
        hood = Hood.objects.get(id =id)
    except ObjectDoesNotExist:
        return Http404
    request.user.profile.hood = hood
    request.user.profile.save()
    return redirect('index')


def leave_hood(request, id):
    try:
        hood = Hood.objects.get(id =id)
    except ObjectDoesNotExist:
        return Http404
    request.user.profile.hood = None
    request.user.profile.save()
    return redirect('index') 



def search_business(request):
    if request.method == 'GET':
        name = request.GET.get('title')

        results = Business.objects.filter(business_name__icontains=name).all()
        # print(results)
        message = f'name'
        
        context = {'results': results, 'message': message}
        return render(request, 'results.html', context)

    else:
        message = "You haven't searched for any business"
    return render(request, 'hood/search_business.html')


def hood_residents(request, hood_id):
    hood = Hood.objects.get(id=hood_id)
    residents = Profile.objects.filter(hood = hood)

    context = {'residents':residents}
    return render(request, 'hood/residents.html', context) 
