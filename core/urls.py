from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('consultancy/', views.consultancy, name='consultancy'),
    path('hackathon/', views.hackathon, name='hackathon'),
    path('messages/', views.messages_dashboard, name='messages_dashboard'),
]


