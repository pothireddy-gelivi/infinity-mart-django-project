from django.shortcuts import render, redirect
from accounts.forms import *
from accounts.models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                phone_number = form.cleaned_data['phone_number']
                password = form.cleaned_data['password']
                username = email.split('@')[0]
                user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.phone_number = phone_number 
                user.save()
                messages.success(request, 'Registration successful!')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Registration failed: {str(e)}')
                return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
           
            
    
    return render(request, 'accounts/register.html', context)
    
def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout(request):    
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')
   