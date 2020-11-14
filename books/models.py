from django.db import models
from login.models import User


class BookManager(models.Manager):
    def add_book(self, form_data, user_id):
        Book.objects.create(
            title=form_data["title"],
            desc=form_data["desc"],
            uploaded_by=User.objects.get(id=user_id),
        ).favorites.add(User.objects.get(id=user_id))

    def updates(self, form_data, book_id):
        this_book = Book.objects.get(id=book_id)
        if "delete" in form_data:
            this_book.delete()
        else:
            for key in ("title", "desc"):
                if getattr(this_book, key) != form_data[key]:
                    this_book.__dict__[key] = form_data[key]
            this_book.save()

    def validate(self, form_data):
        errors = {}
        if not form_data["title"]:
            errors["title"] = "Title is required"
        if len(form_data["desc"]) < 5:
            errors["desc"] = "Description must be longer."
        return errors

    def favorite(self, book_id, user_id):
        this_book = Book.objects.get(id=book_id)
        this_user = User.objects.get(id=user_id)
        if this_user in this_book.favorites.all():
            this_book.favorites.remove(this_user)
        else:
            this_book.favorites.add(this_user)


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="books_uploaded"
    )
    favorites = models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()
