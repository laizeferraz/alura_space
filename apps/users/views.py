from django.shortcuts import render, redirect

from apps.users.forms import UserLoginForm, UserRegisterForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

def view_login(request):
    form = UserLoginForm()

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form["username"].value()
            password = form["password"].value()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'{username} logged in successfully')
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('login')
    
    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
          username=form["username"].value()
          email=form["email"].value()
          password=form["password"].value()

          if User.objects.filter(username=username).exists():
              messages.error(request, 'Username already exists')
              return redirect('register')

          user = User.objects.create_user(username, email, password)
          user.save()
          messages.success(request, f'{username} registered successfully')
          return redirect('login')
        
    return render(request, 'users/register.html', {'form': form})

def view_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')