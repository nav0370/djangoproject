from django.contrib import admin
from django.urls import path
from register import views

urlpatterns = [
    path("", views.index, name='register'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact')
]
