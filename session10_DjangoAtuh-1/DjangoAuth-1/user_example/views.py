from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'user_example/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        
        user = authenticate(username=username, password=password)
        
        login(request, user)
        
        return redirect('home')
        
    else:
        form = UserCreationForm()
        
    context = {
        'form': form,
    }
    return render(request, 'user_example/register.html', context)
