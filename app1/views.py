from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def password_reset(request):
    return render(request, 'password-reset.html')
def register(request):
    return render(request, 'register.html')
def contact(request):
    return render(request, 'contact.html')
def error_404(request):
    return render(request, '404.html')
def account(request):
    return render(request, 'account.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')  # Make sure 'services.html' exists in your templates
