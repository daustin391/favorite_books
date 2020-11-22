import bcrypt
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def index(request):
    if "id" in request.session:
        return success_redirect(request, request.session["id"])
    else:
        return render(request, "index.html")


def success_redirect(request, user_id):
    request.session["id"] = user_id
    return redirect("/books")


def register(request):
    if request.method == "POST":
        errors = User.objects.validate(request.POST)
        if errors:
            for msg in errors.values():
                messages.error(request, msg)
        else:
            password = request.POST["password"]
            hashword = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(
                username=request.POST["username"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                password=hashword,
            )
            return success_redirect(request, User.objects.last().id)
    return redirect("/")


def login(request):
    if request.method == "POST":
        this_user = User.objects.filter(email=request.POST["email"])
        if this_user and bcrypt.checkpw(
            request.POST["password"].encode(), this_user[0].password.encode()
        ):
            return success_redirect(request, this_user[0].id)
        else:
            messages.error(request, "Invalid login")

    return redirect("/")


def logout(request):
    request.session.flush()
    return redirect("/")


def username(request):
    if request.method == "POST":
        context = {}
        for this_user in User.objects.all():
            if request.POST["username"] == this_user.username:
                context = {"used": True}
    return render(request, "partial.html", context)


def usersearch(request):
    if request.method == "POST":

        context = {
            "all_users": User.objects.filter(
                username__startswith=request.POST["search"]
            )
        }

        return render(request, "usersearch.html", context)
    else:
        return redirect("/")
