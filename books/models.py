from django.db import models
from login.models import User


class BookManager(models.Manager):
    def add_book(self, form_data, user_id):
        Book.objects.create(
            title=form_data["title"],
            desc=form_data["desc"],
            uploaded_by=User.objects.get(id=user_id),
        )


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="books_uploaded"
    )
    objects = BookManager()