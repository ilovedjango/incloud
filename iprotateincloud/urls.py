"""iprotateincloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from pool import views
from pool.views import index, servers, pva, Job, ServerRequest, subscription, PvaRequest, ForwardedNumbersRequest


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^servers/$', views.servers, name='servers'),
    url(r'^numbers/$', views.numbers, name='numbers'),
    url(r'^ForwardedNumbersRequest/$', views.ForwardedNumbersRequest, name='ForwardedNumbersRequest'),
    url(r'^pva/$', views.pva, name='pva'),
    url(r'^PvaRequest/$', views.PvaRequest, name='PvaRequest'),
    url(r'^Job/$', views.Job, name='Job'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^ServerRequest/$', views.ServerRequest, name='ServerRequest'),
    url(r'^subscription/$', views.subscription, name='subscription'),
]
