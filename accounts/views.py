from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error': error_message})
    
    return render(request, 'login.html')


@require_http_methods(["GET", "POST"])
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        email = request.POST.get('email', '')
        
        if password != password_confirm:
            error_message = 'Passwords do not match'
            return render(request, 'signup.html', {'error': error_message})
        
        if User.objects.filter(username=username).exists():
            error_message = 'Username already exists'
            return render(request, 'signup.html', {'error': error_message})
        
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('home')
    
    return render(request, 'signup.html')


@login_required(login_url='login')
def home_view(request):
    return render(request, 'home.html', {'user': request.user})


def logout_view(request):
    logout(request)
    return redirect('login')
