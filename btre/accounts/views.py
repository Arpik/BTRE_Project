from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2'] 

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                # Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is taken')
                    return redirect('register')
                else:
                    return
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.htm')

def login(request):
    if request.method == 'POST':
        # Login User 
        return
    else:
        return render(request, 'accounts/register.htm')

    return render(request, 'accounts/login.htm')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.htm')