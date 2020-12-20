from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.registration),
    path('login', views.loginning),
    path('diarymain', views.diarymain, name = "diarymain"),
    path('diarycreate', views.diarycreating, name = "diarycreate"),
    path('diarydelete', views.diarydelete)
]