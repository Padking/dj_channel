from django.urls import path

from . import views

urlpatterns = [
    path("", views.userschannels, name="index"),
]
