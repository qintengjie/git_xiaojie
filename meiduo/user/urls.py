from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    #  用户登陆页面
    url(r'^login/$', views.UserLogin.as_view(),name='login'),
]
