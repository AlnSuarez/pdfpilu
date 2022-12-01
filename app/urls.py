from django.contrib import admin
from django.urls import path, include
from .views import home,pdf, order


urlpatterns = [
    path('', home, name="home"),
    path('pdf', pdf, name="pdf"),
    path('order', order, name="order")
]
