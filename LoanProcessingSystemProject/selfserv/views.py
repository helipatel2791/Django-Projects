from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, 'register.html', {'form': f})

@login_required
def home(request):
    return render(request, 'home_2.html')

def logout(request):
    auth.logout(request)
    return render(request,'blog/logout.html')