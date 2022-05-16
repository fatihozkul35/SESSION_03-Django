from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages
from .forms import UserForm, UserProfile
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def register(request):

    form_user = UserForm(request.POST or None)
    form_profile = UserProfile(request.POST or None)

    if form_user.is_valid() and form_profile.is_valid():
        user = form_user.save()
        profile = form_profile.save(commit=False)
        profile.user = user

        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']

        profile.save()
        login(request,user)
        messages.success(request,'Register successful')

        return redirect('home')
    
    context = {
        'form_user':form_user,
        'form_profile': form_profile
    }

    return render(request, 'users/register.html', context)

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        # username = form.cleaned_data.get("username")
        # password = form.cleaned_data.get("password")

        # user = authenticate(username=username, password=password)
        user = form.get_user()
        if user:
            messages.success(request, "Login Successfull")
            login(request,user)
            return redirect('home')

    return render(request, 'users/user_login.html', {"form":form})

def user_logout(request):
    messages.success(request,'You logged out!')
    logout(request)
    return redirect('home')