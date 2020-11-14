from django.shortcuts import render, redirect
from login.models import User
from .models import Book


def index(request):
    context = {"this_user": User.objects.get(id=request.session["id"])}
    return render(request, "books.html", context)


def add_book(request):
    if request.method == "POST":
        Book.objects.add_book(request.POST, request.session["id"])
    return redirect("/books")