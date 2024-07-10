from django.shortcuts import render

from users.forms import UserLoginForm, UserRegisterForm

def login(request):
    form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
