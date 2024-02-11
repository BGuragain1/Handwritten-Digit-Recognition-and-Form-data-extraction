from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.startPage,name="home"),
    path('login', views.login,name="login"),
    path('signup', views.signup,name="signup"),
    path('logout', views.logout,name="logout"),
    path('home',views.homePage,name="homePage"),
    path('about',views.about,name="about"),
    path('feedback',views.feedback,name="feedback"),
    path('base',views.base, name="base"),
]
