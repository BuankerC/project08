from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=200)
    description = models.TextField()
    genre_id = models.IntegerField()

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Review(models.Model):
    content = models.CharField(max_length=100)
    score = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)