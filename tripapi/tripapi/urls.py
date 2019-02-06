"""tripapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import patterns, url

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', 'home'),
    
    #api urls
    url(r'^api/v1/tripdetails/$', 'detail_collection'),
    url(r'^api/v1/posts/(?P<pk>[0-9]+)$', 'detail_element'),

]



















































































