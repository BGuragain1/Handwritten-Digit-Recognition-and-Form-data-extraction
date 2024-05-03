from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.startPage,name="home"),
    path('login', views.Login,name="login"),
    path('signup', views.signup,name="signup"),
    path('logout', views.logout_view,name="logout"),
    path('home',views.homePage,name="homePage"),
    path('edit',views.editForm,name="editForm"),
    path('form',views.details,name="details"),
    path('search',views.searchDetails,name="searchDetails"),
    path('student',views.addStudents,name="addStudents"),
    path('formPhoto',views.uploadForms, name="uploadForms"),
    path('details',views.viewDetails,name="viewDetails")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.MEDIA_URL1, document_root=settings.MEDIA_ROOT1)+ static(settings.MEDIA_URL2, document_root=settings.MEDIA_ROOT2)
