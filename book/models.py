from django.db import models

# Create your models here.


class Book(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.name
