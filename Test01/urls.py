"""Test01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from Login import views as login_views
from Register import  views as register_views
from Authenticate import  views as authenticate_views
from OperateFile import views as operate_views
from lll import views as lll_views


urlpatterns = [
url(r'^admin/', admin.site.urls),
    url(r'^login/', login_views.login),
    url(r'^register/', register_views.register),
    url(r'^authenticate/', authenticate_views.authenticate),
    url(r'^lll/', lll_views.lll),
    url(r'^user/', lll_views.user),
    url(r'^test/', lll_views.demo),
    #url(r'^readfile/', lll_views.readfile),

    url(r'^readfile/', operate_views.operatefile),
    url(r'^userinfo/', operate_views.user_info),
]
