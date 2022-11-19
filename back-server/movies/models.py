from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    released_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500)
    adult = models.BooleanField()
    genres = models.ManyToManyField(Genre)
    actors_data = models.CharField(max_length=500)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
  
    def __str__(self):
        return self.title

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def username(self):
        return self.user.username

    def __str__(self):
        return f'{self.movie} | {self.score} | {self.comment}'

