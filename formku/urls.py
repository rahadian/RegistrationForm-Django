"""formku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from users import views
from django.conf.urls import handler404
app_name ='users'
handler404='users.views.page_not_found'
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('users.urls')),
    url(r'^users/', include('users.urls',namespace="users")),
    url(r'^$', views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name':'users/login.html'}, name='login'),
    url(r'^logout/$',auth_views.logout,{'template_name':'users/logout.html'},name='logout'),
]
