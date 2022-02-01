from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='ap-token')
]
