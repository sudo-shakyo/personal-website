"""codewithshakyo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from __future__ import annotations
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from blog import views
from blog.views import announcements
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls import url
from django.conf import settings
admin.site.site_header = "CodeWithShakyo Admin"
admin.site.site_title = "CodeWithShakyo Portal"
admin.site.index_title = "Welcome"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('about', views.about, name="about"),
    path('announcements', views.announcements, name="announcements"),
    path('message', views.message, name="message"),
    path('home', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('info', views.index, name="info"),
    path('login/', views.login_user, name="login"),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('change_password', views.change_password, name='change_password'),
    path('terms', views.terms, name='terms'), 
    path('info/', views.personal_info, name='info'),

   #url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
   #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 


]
