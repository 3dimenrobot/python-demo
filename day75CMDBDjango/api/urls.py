
from django.contrib import admin
from django.urls import path

from  django.conf.urls import url,include

from . import views

urlpatterns = [
    path('asset/', views.asset),
    path('test/', views.test),

]
