from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("login", views.login),
    path("books/", include("books.urls")),
    path("logout", views.logout),
]
