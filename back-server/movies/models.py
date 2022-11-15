from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    released_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    # backdrop_path = models.CharField(max_length=500)
    adult = models.BooleanField()
    genres = models.ManyToManyField(Genre)
    actors_data = models.CharField(max_length=500)
  
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

