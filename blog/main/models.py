from django.db import models

import datetime


class User(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name="author",
        on_delete=models.CASCADE
    )
    published = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(
        Category,
        # verbose_name="category",
        on_delete=models.CASCADE,
        # related_name='category_parent',
        # null=True
    )
    published_at = models.DateTimeField(default=datetime.datetime.now, blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True)






