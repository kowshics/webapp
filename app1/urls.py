from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),    
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('password-reset/', views.password_reset, name='password-reset'),
    path('404/', views.error_404, name='404'),  
    path('services/', views.services, name='services'),
    path('404/', views.error_404, name='404'),
]