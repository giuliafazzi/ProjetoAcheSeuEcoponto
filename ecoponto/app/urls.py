from django.contrib import admin
from django.urls import path, include
from app.views import IndexView

app_name = 'app'

urlpatterns = [
    path('', IndexView, name='index')
]
