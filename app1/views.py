from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def account(request):
    return render(request, 'account.html')  
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')
def faq(request):
    return render(request, 'faq.html')
def terms(request):
    return render(request, 'terms.html')
def privacy(request):
    return render(request, 'privacy.html')
def error_404_view(request, exception):
    return render(request, '404.html', status=404)  
def error_500_view(request):
    return render(request, '500.html', status=500)
def error_403_view(request, exception):
    return render(request, '403.html', status=403)