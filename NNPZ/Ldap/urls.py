from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Ldap_connect, name='Ldap'),
    path('ldapi', department, name='ld_conn')
]
