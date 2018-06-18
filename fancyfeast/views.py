from django.shortcuts import redirect
from django.http import HttpResponse

def login_redirect(request):
    return redirect('/account/login')

def home(request):
    return HttpResponse('FancyFeast homepage')