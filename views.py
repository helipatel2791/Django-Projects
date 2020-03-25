from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Users
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            username_entry = form.cleaned_data['username']
            password_entry = form.cleaned_data['password1']
            user_record = Users(username = username_entry, user_password = password_entry)
            user_record.save()
            return redirect('/users/login/')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

def intimateuser(request):
    return HttpResponse('Congratulations! You are logged in')

def login(request):

    if request.method == 'POST':

        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():

            if Users.objects.filter(username=loginForm.cleaned_data['userid'] , user_password=loginForm.cleaned_data['passwd']).exists():
                messages.success(request, "You are logged in!")
                return redirect('/users/intimateuser/')
             

    else:
        form = LoginForm()
    return render(request,'session_login.html',{'form':form})
    
