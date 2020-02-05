from django.shortcuts import render, redirect
from django.contrib import messages 

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Register User 
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