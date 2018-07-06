from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import RegistrationForm

def login_redirect(request):
    return redirect('/accounts/login')

def home(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # cleaned (normalized) data
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            # returns User object if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('accounts:view_profile'))
        return render(request, 'accounts/home.html', {'form':form})
    else:
        form = RegistrationForm()
        return render(request, 'accounts/home.html', {'form':form})
