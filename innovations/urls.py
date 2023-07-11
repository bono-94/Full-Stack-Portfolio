"""
Innovations URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls'), name='projects_urls'),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
]
