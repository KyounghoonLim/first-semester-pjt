from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=20)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    overview = models.TextField()
    vote_average = models.FloatField(default=10)
    genres = models.ManyToManyField(Genre)
    poster_path = models.TextField(null=True)
    release_date = models.DateField()

    def __str__(self):
        return self.title 
    
class Review(models.Model):
    content = models.CharField(max_length=20)
    score = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)          
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content