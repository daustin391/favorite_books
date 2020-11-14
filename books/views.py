from django.shortcuts import render
from login.models import User


def index(request):
    context = {"this_user": User.objects.get(id=request.session["id"])}
    return render(request, "books.html", context)