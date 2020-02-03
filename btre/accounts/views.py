from django.shortcuts import render, redirect

def register(request):
    return render(request, 'accounts/register.htm')

def login(request):
    return render(request, 'accounts/login.htm')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.htm')