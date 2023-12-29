from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name = "home"),
    path('registration',views.registration),
    path('read',views.read,name = "read"),
    path('update/<int:id>',views.update,name = "update"),
    path('delete/<int:id>',views.delete,name = "delete"),
    path('request',views.request,name = 'request'),

]
 