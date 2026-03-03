from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('docshell/', views.docshell, name='docshell'),
    path('expert/', views.expert, name='expert'),
    path('contacts/', views.contacts, name='contacts'),
    path('privacy/', views.privacy, name='privacy'),
    path('consent/', views.consent, name='consent'),
]