from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    created_in = models.DateTimeField(auto_now_add=True)
    modified_in = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class News(models.Model):
    created_in = models.DateTimeField(auto_now_add=True)
    modified_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
