from django.shortcuts import render, redirect
from django.contrib import messages
from login.models import User
from .models import Book


def index(request):
    context = {
        "this_user": User.objects.get(id=request.session["id"]),
        "all_books": Book.objects.all(),
    }
    return render(request, "books.html", context)


def add_book(request):
    if request.method == "POST":
        errors = Book.objects.validate(request.POST)
        if errors:
            for msg in errors.values():
                messages.error(request, msg)
        else:
            Book.objects.add_book(request.POST, request.session["id"])
    return redirect("/books")


def details(request, book_id):
    this_user = User.objects.get(id=request.session["id"])
    this_book = Book.objects.get(id=book_id)
    context = {
        "this_book": this_book,
        "this_user": this_user,
    }
    if this_book.uploaded_by == this_user:
        return render(request, "update.html", context)
    else:
        return render(request, "details.html", context)


def update(request, book_id):
    if request.method == "POST":
        errors = Book.objects.validate(request.POST)
        if errors:
            for msg in errors.values():
                messages.error(request, msg)
            return redirect(f"/books/{book_id}")
        else:
            Book.objects.updates(request.POST, book_id)
    return redirect("/books")


def favorite(request, book_id):
    Book.objects.favorite(book_id, request.session["id"])
    return redirect(f"/books/{book_id}")
