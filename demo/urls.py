from django.contrib import admin

from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('dashboardMainPage/',views.dashboardMainPage,name='dashboardMainPage'),
    path('signup/',views.signup,name='signup'),
]