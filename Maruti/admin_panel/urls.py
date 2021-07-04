from django.urls import path
from django.contrib import admin
from admin_panel import views
urlpatterns = [
    path('index/',views.index)
]