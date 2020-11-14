from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("add", views.add_book),
    path("<int:book_id>", views.details),
    path("<int:book_id>/update", views.update),
    path("<int:book_id>/favorites", views.favorite),
]
