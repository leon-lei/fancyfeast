from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def login_redirect(request):
    return redirect('/account/login')

def home(request):
    return redirect(reverse('accounts:home'))